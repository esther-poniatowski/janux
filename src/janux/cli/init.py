"""
janux.cli.init
==============

Initialize Janux configuration structure.

Commands
--------
init
    Create the default directory layout for Janux configuration.
"""

from pathlib import Path

import typer

from janux.initialization import create_config_structure

app = typer.Typer()


@app.callback(invoke_without_command=True)
def init(
    destination: Path = typer.Option(
        ".",
        help="Target directory for Janux configuration.",
        exists=True,
        file_okay=False,
        resolve_path=True,
    ),
) -> None:
    """Initialize the default structure for Janux in the specified destination."""
    create_config_structure(destination)
    typer.echo(f"Janux configuration initialized in: {destination / 'config' / 'janux'}")
