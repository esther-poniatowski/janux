"""
janux.cli.init
==============

Initialize Janux configuration structure.

Commands
--------
init
    Create the directory layout for Janux configuration, by default under
    ``config/local/janux/``, or at the places given by its options.

Notes
-----
The root is resolved from ``--root``, then from the environment variable ``JANUX_ROOT``, then
from the current folder. Janux has no settings file, so the command does not search the
ancestors of the current folder.
"""

from pathlib import Path

import typer

from janux.initialization import JanuxInitRequest, create_config_structure
from janux.initialization.setup import DEFAULT_CONFIG_LAYOUT, JanuxConfigLayout

app = typer.Typer()


@app.command("init")
def init(
    root: Path = typer.Option(
        ".",
        "--root",
        "-r",
        envvar="JANUX_ROOT",
        help="Folder in which the configuration tree is created.",
        file_okay=False,
        resolve_path=True,
    ),
    config_root: str = typer.Option(
        DEFAULT_CONFIG_LAYOUT.config_root,
        help="Folder of the configuration, relative to the root.",
    ),
    janux_root: str = typer.Option(
        DEFAULT_CONFIG_LAYOUT.janux_root,
        help="Folder of Janux inside the configuration folder.",
    ),
    subdirectory: list[str] = typer.Option(
        list(DEFAULT_CONFIG_LAYOUT.subdirectories),
        "--subdirectory",
        help="Subdirectory to create in the folder of Janux; repeat the option for several.",
    ),
) -> None:
    """Initialize the structure for Janux in the root folder."""
    try:
        layout = JanuxConfigLayout(
            config_root=config_root, janux_root=janux_root, subdirectories=tuple(subdirectory)
        )
    except ValueError as error:
        raise typer.BadParameter(str(error)) from error
    request = JanuxInitRequest(destination=root, layout=layout)
    try:
        request = create_config_structure(request)
    except FileExistsError as error:
        typer.echo(f"Error: {error}", err=True)
        raise typer.Exit(code=2) from error
    typer.echo(f"Janux configuration initialized in: {request.config_root}")
