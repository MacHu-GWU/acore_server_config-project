# -*- coding: utf-8 -*-

import typing as T
import dataclasses

if T.TYPE_CHECKING:  # pragma: no cover
    from .main import Env


@dataclasses.dataclass
class Server:
    id: T.Optional[str] = dataclasses.field(default=None)
    db_admin_password: T.Optional[str] = dataclasses.field(default=None)
    db_username: T.Optional[str] = dataclasses.field(default=None)
    db_password: T.Optional[str] = dataclasses.field(default=None)


@dataclasses.dataclass
class ServerMixin:
    servers: T.Dict[str, Server] = dataclasses.field(default_factory=dict)

    @property
    def server_blue(self) -> Server:
        return self.servers["blue"]

    @property
    def server_green(self) -> Server:
        return self.servers["green"]
