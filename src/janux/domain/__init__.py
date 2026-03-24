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
