import logging
from asyncio import StreamReader
from typing import Optional, Iterable

from pyfsftpserver.base.utils import IpEndpoint

from pyfsftpserver.base.prorocols.data_channel import DataProtocol
from .mlsx_format import MlsxFormatter, FileListFormatter, ListFormatter
from ..messages import Reply, UnknownCommandReply
from ..shell import FtpShell, DirectoryNotEmpty, FileInfo

logger = logging.getLogger(__name__)


class ShellHandlerMixin:
    shell: Optional[FtpShell]
    implementation_context: 'CommandChannelContext'

    mlsx_formatter = MlsxFormatter()
    list_formatter = FileListFormatter()

    async def do_cmd_cwd(self, path):
        newcwd = await self.shell.change_dir(path)
        return Reply("200", f"OK, new cwd is {newcwd!r}")

    async def do_cmd_cdup(self, path):
        newcwd = await self.shell.change_dir_up()
        return Reply("200", f"OK, new cwd is {newcwd!r}")

    async def do_cmd_pwd(self, arg):
        cwd = await self.shell.get_cwd()
        return Reply("200", cwd)

    async def do_cmd_list(self, path):
        return await self._relpy_files(path, self.list_formatter)

    async def do_cmd_mlsd(self, path):
        return await self._relpy_files(path, self.mlsx_formatter)

    async def do_cmd_retr(self, path):
        datastream = await self.shell.open_read(path)
        return Reply(payload=self._stream_data(datastream))

    async def do_cmd_stor(self, path):
        streamwriter = await self.shell.open_write(path)
        return Reply(sink=streamwriter)

    async def do_cmd_mkd(self, path):
        await self.shell.make_dir(path)
        return Reply("250", "directory created")

    async def do_cmd_rmd(self, path):
        try:
            await self.shell.remove_dir(path)
        except DirectoryNotEmpty:
            return Reply("450", "directory not empty")
        return Reply("250", "directory deleted")

    async def do_cmd_dele(self, path):
        await self.shell.remove_file(path)
        return Reply("250", "file removed")

    def _format_textlines(self, lines):
        for line in lines:
            yield f"{line}\r\n".encode(encoding=self.implementation_context.encoding)

    async def _relpy_files(self, path: str, formatter: ListFormatter):
        files = await self.shell.list_dir(path)
        return self._format_files_reply(files, formatter)

    def _format_files_reply(self, files: Iterable[FileInfo], formatter: ListFormatter):
        lines = formatter.format_all(files)
        payload = self._format_textlines(lines)
        return Reply(payload=payload)

    async def _stream_data(self, datastream: StreamReader):
        while True:
            chunk = datastream.read(self.implementation_context.buffer_size)
            if not chunk:
                return
            yield chunk


class ConnectionHandlerMixin:
    features: Iterable[str]
    system_string: str
    data_protocol: DataProtocol
    implementation_context: 'CommandChannelContext'
    running: bool
    shell: Optional[FtpShell]
    command_local_endpoint: IpEndpoint
    _pending_user: Optional[str]

    async def do_cmd_pasv(self, arg):
        if self.data_protocol.freeze_epsv:
            return Reply("520", f"Only EPSV data connection commands are allowed, EPSV ALL was already calledc")

        data_info = await self.data_protocol.enter_passive_mode()
        addr = self.command_local_endpoint.address.replace('.', ",")  # TODO: ipv6? Why is TotalCommander not using EPSV?
        port = f"{data_info.port // 256},{data_info.port % 256}"
        return Reply("227", f"Entering passive mode {addr},{port}")

    async def do_cmd_epsv(self, arg):
        if arg == 'ALL':
            self.data_protocol.freeze_epsv = True
            return Reply("200", f"Entered EPSV exclusive mode, rejecting all other data connection setup commands")
        if arg:
            return Reply("500", f"Protocol parameter not supported yet.")
        info = await self.data_protocol.enter_passive_mode()
        return Reply("229", f"Entering Extended Passive Mode  (|||{info.port}|)")

    async def do_cmd_user(self, arg):
        self._pending_user = arg
        self._close_shell()
        self.shell = await self.implementation_context.shell_factory(arg)

    async def do_cmd_quit(self, arg):
        self.running = False
        return Reply("221", "goodbye")

    async def do_cmd_syst(self, arg):
        return Reply("215", self.system_string)

    async def do_cmd_type(self, arg):
        if arg != 'A':
            return Reply("500", "Only TYPE A is supported")
        return Reply("200", "TYPE is now ASCII")

    async def do_cmd_port(self, arg):
        return Reply("500", "active mode not supported")

    async def do_cmd_feat(self, path):
        return Reply("211", "OK", items=self.features)

    async def do_cmd_opts(self, opt: Optional[str]):
        if not opt:
            return Reply("211", "OK")
        if opt.upper() == 'UTF8 ON':
            return Reply("211", "OK")
        return Reply("502", "Option not supported")

    def _close_shell(self):
        pass


class CommandHandler(ShellHandlerMixin, ConnectionHandlerMixin):
    system_string = "unix python pyfsftpserver"
    features = ("MLSD", "MLST", "PASV", "EPSV", "EPRT", "UTF8")
    running: bool

    def __init__(self, data_protocol, command_local_endpoint, implementation_context):
        self.implementation_context = implementation_context
        self.shell = None
        self.data_protocol = data_protocol
        self._pending_user = None
        self.running = True
        self.command_local_endpoint = command_local_endpoint

    async def process(self, cmd, arg) -> Reply:
        handler = getattr(self, f"do_cmd_{cmd}", None)
        if handler is None:
            return UnknownCommandReply(cmd)
        try:
            return await handler(arg)
        except Exception as ex:
            logger.exception(f"Error while processing command {cmd}", ex)
            return Reply("451", f"internal error during command {cmd}: {ex}")

    def close(self):
        self._close_shell()

    def _close_shell(self):
        if self.shell is not None:
            self.shell.close()
            self.shell = None


class CommandChannelContext:
    encoding: str
    buffer_size: int

    async def shell_factory(self, username):
        raise NotImplementedError()
