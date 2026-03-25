"""
janux.initialization.setup
==========================

Setup routines for initializing the Janux configuration structure.

Functions
---------
create_config_structure
    Create the default directory layout for Janux configuration.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class JanuxConfigLayout:
    """Declarative description of the Janux config tree."""

    config_root: str = "config"
    janux_root: str = "janux"
    subdirectories: tuple[str, ...] = ("hosts", "credentials", "profiles")

    def __post_init__(self) -> None:
        if not self.config_root.strip():
            raise ValueError("config_root must not be empty")
        if not self.janux_root.strip():
            raise ValueError("janux_root must not be empty")
        if not self.subdirectories:
            raise ValueError("subdirectories must not be empty")
        normalized = tuple(subdir.strip() for subdir in self.subdirectories)
        if any(not subdir for subdir in normalized):
            raise ValueError("subdirectories must not contain empty names")
        object.__setattr__(self, "subdirectories", normalized)

    def root_path(self, destination: Path) -> Path:
        return destination / self.config_root / self.janux_root

    def child_paths(self, destination: Path) -> tuple[Path, ...]:
        root = self.root_path(destination)
        return tuple(root / subdir for subdir in self.subdirectories)


DEFAULT_CONFIG_LAYOUT = JanuxConfigLayout()


@dataclass(frozen=True)
class JanuxInitRequest:
    """Validated input model for the init workflow."""

    destination: Path
    layout: JanuxConfigLayout = DEFAULT_CONFIG_LAYOUT

    def __post_init__(self) -> None:
        destination = self.destination.expanduser()
        if destination.exists() and destination.is_file():
            raise ValueError("destination must be a directory path")
        object.__setattr__(self, "destination", destination)

    @property
    def config_root(self) -> Path:
        return self.layout.root_path(self.destination)


def _coerce_request(destination: Path | JanuxInitRequest) -> JanuxInitRequest:
    if isinstance(destination, JanuxInitRequest):
        return destination
    return JanuxInitRequest(destination=destination)


def create_config_structure(destination: Path | JanuxInitRequest) -> JanuxInitRequest:
    """Create a basic Janux configuration directory structure.

    Creates a ``config/janux/`` tree under *destination* with placeholder
    sub-directories for hosts, credentials, and profiles.

    Parameters
    ----------
    destination : Path | JanuxInitRequest
        Root directory or validated init request under which the configuration
        tree is created.
    """
    request = _coerce_request(destination)
    for subdir in request.layout.child_paths(request.destination):
        subdir.mkdir(parents=True, exist_ok=True)
    return request
