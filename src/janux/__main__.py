"""
Entry point for the `janux` package, invoked as a module.

Usage
-----
To launch the command-line interface, execute::

    python -m janux


See Also
--------
janux.cli: Module implementing the application's command-line interface.
"""
from .cli import app

app()
