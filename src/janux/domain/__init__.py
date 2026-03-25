"""
janux.domain
=============

Domain model for Janux.

Provides typed containers representing SSH connection concepts.

Classes
-------
ConnectionSpec
    Specification for an SSH connection.
HostConfig
    Configuration for a remote host.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ConnectionSpec:
    """Specification for an SSH connection.

    Attributes
    ----------
    host : str
        Hostname or IP address of the remote server.
    user : str
        Username for authentication.
    port : int
        SSH port number.
    identity_file : Path | None
        Path to the private key file, if any.
    """

    host: str
    user: str
    port: int = 22
    identity_file: Path | None = None

    def __post_init__(self) -> None:
        host = self.host.strip()
        user = self.user.strip()
        if not host:
            raise ValueError("host must not be empty")
        if not user:
            raise ValueError("user must not be empty")
        if not 1 <= self.port <= 65535:
            raise ValueError("port must be between 1 and 65535")
        object.__setattr__(self, "host", host)
        object.__setattr__(self, "user", user)
        if self.identity_file is not None:
            object.__setattr__(
                self,
                "identity_file",
                self.identity_file.expanduser(),
            )


@dataclass(frozen=True)
class HostConfig:
    """Configuration for a remote host.

    Attributes
    ----------
    alias : str
        Short label used to reference this host.
    connection : ConnectionSpec
        Connection details for the host.
    """

    alias: str
    connection: ConnectionSpec

    def __post_init__(self) -> None:
        alias = self.alias.strip()
        if not alias:
            raise ValueError("alias must not be empty")
        object.__setattr__(self, "alias", alias)
