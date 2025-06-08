"""
Command-line entry point for the `janux` package.

Usage
-----
To invoke the package::

    python -m janux


See Also
--------
janux.cli: Command-line interface module for the package.
"""
from .cli import app

app()
