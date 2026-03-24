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

from pathlib import Path


def create_config_structure(destination: Path) -> None:
    """Create a basic Janux configuration directory structure.

    Creates a ``config/janux/`` tree under *destination* with placeholder
    sub-directories for hosts, credentials, and profiles.

    Parameters
    ----------
    destination : Path
        Root directory under which the configuration tree is created.

    Raises
    ------
    FileNotFoundError
        If *destination* does not exist.
    """
    root = destination / "config" / "janux"
    for subdir in ("hosts", "credentials", "profiles"):
        (root / subdir).mkdir(parents=True, exist_ok=True)
