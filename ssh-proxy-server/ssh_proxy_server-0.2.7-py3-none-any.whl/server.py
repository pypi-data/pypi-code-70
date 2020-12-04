import logging
import os
import select
import socket
import time
import threading

from paramiko import RSAKey

from ssh_proxy_server.session import Session


class SSHProxyServer:
    HOST_KEY_LENGTH = 2048
    SELECT_TIMEOUT = 0.5

    def __init__(
        self,
        listen_address,
        key_file=None,
        ssh_interface=None,
        scp_interface=None,
        sftp_interface=None,
        sftp_handler=None,
        authentication_interface=None,
        authenticator=None,
        transparent=False
    ):
        self._threads = []
        self._hostkey = None

        self.listen_address = listen_address
        self.running = False

        self.key_file = key_file

        self.ssh_interface = ssh_interface
        self.scp_interface = scp_interface
        self.sftp_handler = sftp_handler
        self.sftp_interface = self.sftp_handler.get_interface() or sftp_interface
        self.authentication_interface = authentication_interface
        self.authenticator = authenticator
        self.transparent = transparent

    @property
    def host_key(self):
        if not self._hostkey:
            if not self.key_file:
                self._hostkey = RSAKey.generate(bits=self.HOST_KEY_LENGTH)
                logging.warning("created temporary private key!")
            else:
                if not os.path.isfile(self.key_file):
                    raise FileNotFoundError("host key '{}' file does not exist".format(self.key_file))
                try:
                    self._hostkey = RSAKey(filename=self.key_file)
                except Exception:
                    logging.error('only rsa key files are supported!')
        return self._hostkey

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if self.transparent:
            sock.setsockopt(socket.SOL_IP, socket.IP_TRANSPARENT, 1)
        sock.bind(self.listen_address)
        sock.listen(5)

        logging.info('listen on %s', self.listen_address)
        self.running = True
        try:
            while self.running:
                readable = select.select([sock], [], [], self.SELECT_TIMEOUT)[0]
                if len(readable) == 1 and readable[0] is sock:
                    client, addr = sock.accept()
                    remoteaddr = client.getsockname()
                    logging.info('incoming connection from %s to %s', str(addr), remoteaddr)

                    thread = threading.Thread(target=self.create_session, args=(client, addr, remoteaddr))
                    thread.start()
                    self._threads.append(thread)
        except KeyboardInterrupt:
            self.running = False
        finally:
            sock.close()
            for thread in self._threads[:]:
                thread.join()

    def create_session(self, client, addr, remoteaddr):
        try:
            with Session(self, client, addr, self.authenticator, remoteaddr) as session:
                if session.start():
                    time.sleep(0.1)
                    if session.ssh and self.ssh_interface:
                        session.ssh = False
                        self.ssh_interface(session).forward()
                    elif session.scp and self.scp_interface:
                        session.scp = False
                        self.scp_interface(session).forward()
                    while True:
                        time.sleep(1)
                else:
                    logging.warning("Session not started")
                    self._threads.remove(threading.current_thread())
        except Exception:
            logging.exception("error handling session")
        logging.info("session closed")
