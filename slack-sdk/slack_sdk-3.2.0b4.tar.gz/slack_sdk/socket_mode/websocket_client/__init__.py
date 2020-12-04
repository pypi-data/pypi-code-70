import logging
import time
from concurrent.futures.thread import ThreadPoolExecutor
from logging import Logger
from queue import Queue
from threading import Lock
from typing import Union, Optional, List, Callable, Tuple

import websocket
from websocket import WebSocketApp

from slack_sdk.socket_mode.client import BaseSocketModeClient
from slack_sdk.socket_mode.listeners import (
    WebSocketMessageListener,
    SocketModeRequestListener,
)
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.web import WebClient


class SocketModeClient(BaseSocketModeClient):
    logger: Logger
    web_client: WebClient
    app_token: str
    wss_uri: Optional[str]
    message_queue: Queue
    message_listeners: List[
        Union[
            WebSocketMessageListener,
            Callable[["BaseSocketModeClient", dict, Optional[str]], None],
        ]
    ]
    socket_mode_request_listeners: List[
        Union[
            SocketModeRequestListener,
            Callable[["BaseSocketModeClient", SocketModeRequest], None],
        ]
    ]

    current_app_executor: ThreadPoolExecutor
    current_app_monitor: ThreadPoolExecutor
    current_app_monitor_started: bool
    message_processor: ThreadPoolExecutor
    message_workers: ThreadPoolExecutor

    current_session: Optional[WebSocketApp]

    auto_reconnect_enabled: bool
    default_auto_reconnect_enabled: bool

    connect_operation_lock: Lock

    on_open_listeners: List[Callable[[WebSocketApp], None]]
    on_message_listeners: List[Callable[[WebSocketApp, str], None]]
    on_error_listeners: List[Callable[[WebSocketApp, Exception], None]]
    on_close_listeners: List[Callable[[WebSocketApp], None]]

    def __init__(
        self,
        app_token: str,
        logger: Optional[Logger] = None,
        web_client: Optional[WebClient] = None,
        auto_reconnect_enabled: bool = True,
        ping_interval: float = 10,
        concurrency: int = 10,
        trace_enabled: bool = False,
        http_proxy_host: Optional[str] = None,
        http_proxy_port: Optional[int] = None,
        http_proxy_auth: Optional[Tuple[str, str]] = None,
        proxy_type: Optional[str] = None,
        on_open_listeners: Optional[List[Callable[[WebSocketApp], None]]] = None,
        on_message_listeners: Optional[
            List[Callable[[WebSocketApp, str], None]]
        ] = None,
        on_error_listeners: Optional[
            List[Callable[[WebSocketApp, Exception], None]]
        ] = None,
        on_close_listeners: Optional[List[Callable[[WebSocketApp], None]]] = None,
    ):
        self.app_token = app_token
        self.logger = logger or logging.getLogger(__name__)
        self.web_client = web_client or WebClient()
        self.default_auto_reconnect_enabled = auto_reconnect_enabled
        self.auto_reconnect_enabled = self.default_auto_reconnect_enabled
        self.ping_interval = ping_interval
        self.wss_uri = self.issue_new_wss_url()
        self.message_queue = Queue()
        self.message_listeners = []
        self.socket_mode_request_listeners = []

        self.current_session = None
        self.current_app_monitor = ThreadPoolExecutor(1)
        self.current_app_monitor_started = False
        self.current_app_executor = ThreadPoolExecutor(1)

        self.connect_operation_lock = Lock()

        self.message_processor = ThreadPoolExecutor(1)
        self.message_processor.submit(self.process_messages)
        self.message_workers = ThreadPoolExecutor(max_workers=concurrency)

        # NOTE: only global settings is provided by the library
        websocket.enableTrace(trace_enabled)

        self.http_proxy_host = http_proxy_host
        self.http_proxy_port = http_proxy_port
        self.http_proxy_auth = http_proxy_auth
        self.proxy_type = proxy_type

        self.on_open_listeners = on_open_listeners or []
        self.on_message_listeners = on_message_listeners or []
        self.on_error_listeners = on_error_listeners or []
        self.on_close_listeners = on_close_listeners or []

    def is_connected(self) -> bool:
        return self.current_session is not None

    def connect(self) -> None:
        def on_open(ws: WebSocketApp):
            if self.logger.level <= logging.DEBUG:
                self.logger.debug("on_open invoked")
            for listener in self.on_open_listeners:
                listener(ws)

        def on_message(ws: WebSocketApp, message: str):
            if self.logger.level <= logging.DEBUG:
                self.logger.debug(f"on_message invoked: (message: {message})")
            self.enqueue_message(message)
            for listener in self.on_message_listeners:
                listener(ws, message)

        def on_error(ws: WebSocketApp, error: Exception):
            self.logger.error(
                f"on_error invoked (error: {type(error).__name__}, message: {error})"
            )
            for listener in self.on_error_listeners:
                listener(ws, error)

        def on_close(ws: WebSocketApp):
            if self.logger.level <= logging.DEBUG:
                self.logger.debug("on_close invoked")
            if self.auto_reconnect_enabled:
                self.logger.info("Received CLOSE event. Going to reconnect...")
                self.connect_to_new_endpoint()
            for listener in self.on_close_listeners:
                listener(ws)

        old_session: Optional[WebSocketApp] = self.current_session
        self.current_session = websocket.WebSocketApp(
            self.wss_uri,
            on_open=on_open,
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
        )
        self.auto_reconnect_enabled = self.default_auto_reconnect_enabled

        def run_current_session():
            self.current_session.run_forever(
                ping_interval=self.ping_interval,
                http_proxy_host=self.http_proxy_host,
                http_proxy_port=self.http_proxy_port,
                http_proxy_auth=self.http_proxy_auth,
                proxy_type=self.proxy_type,
            )

        def monitor_current_session():
            while True:
                time.sleep(self.ping_interval)
                try:
                    if self.auto_reconnect_enabled and (
                        self.current_session is None
                        or self.current_session.sock is None
                    ):
                        self.logger.info(
                            "The session seems to be already closed. Going to reconnect..."
                        )
                        self.connect_to_new_endpoint()
                except Exception as e:
                    self.logger.error(
                        "Failed to check the current session or reconnect to the server "
                        f"(error: {type(e).__name__}, message: {e})"
                    )

        self.current_app_executor.submit(run_current_session)
        if not self.current_app_monitor_started:
            self.current_app_monitor.submit(monitor_current_session)
            self.current_app_monitor_started = True

        self.logger.info("A new session has been established")
        if old_session is not None:
            old_session.close()

    def disconnect(self) -> None:
        self.current_session.close()

    def send_message(self, message: str) -> None:
        if self.logger.level <= logging.DEBUG:
            self.logger.debug(f"Sending a message: {message}")
        self.current_session.send(message)

    def close(self):
        self.auto_reconnect_enabled = False
        self.disconnect()
        self.current_app_monitor.shutdown()
        self.current_app_executor.shutdown()
        self.message_processor.shutdown()
        self.message_workers.shutdown()
