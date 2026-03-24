"""
janux.cli
=========

Command-line interface for the ``janux`` package.

Defines commands available via ``python -m janux`` or ``janux`` if installed as a script.

Commands
--------
info : Display diagnostic information.
init : Initialize Janux configuration structure.

Modules
-------
init
    Initialize Janux configuration structure.

See Also
--------
typer.Typer
    Library for building CLI applications: https://typer.tiangolo.com/
"""

import typer

from janux import info, __version__
from janux.cli.init import app as init_app

app = typer.Typer(add_completion=False, no_args_is_help=True)
app.add_typer(init_app, name="init", help="Initialize Janux configuration structure.")


@app.command("info")
def cli_info() -> None:
    """Display version and platform diagnostics."""
    typer.echo(info())


@app.callback()
def main_callback(
    version: bool = typer.Option(
        False, "--version", "-v", help="Show the package version and exit."
    )
) -> None:
    """Root command for the package command-line interface."""
    if version:
        typer.echo(__version__)
        raise typer.Exit()
