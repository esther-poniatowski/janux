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

from janux.initialization import JanuxInitRequest, create_config_structure

app = typer.Typer()


@app.callback(invoke_without_command=True)
def init(
    destination: Path = typer.Option(
        ".",
        help="Target directory for Janux configuration.",
        file_okay=False,
        resolve_path=True,
    ),
) -> None:
    """Initialize the default structure for Janux in the specified destination."""
    request = JanuxInitRequest(destination=destination)
    request = create_config_structure(request)
    typer.echo(f"Janux configuration initialized in: {request.config_root}")
