"""
janux.cli.init
==============

Initialize Janux configuration structure.

Commands
--------
init
    Create the directory layout for Janux configuration, by default under
    ``config/local/janux/``, or at the places given by its options.
"""

from pathlib import Path
from typing import Optional

import typer
from click.core import ParameterSource

from janux.initialization import JanuxInitRequest, create_config_structure
from janux.initialization.setup import DEFAULT_CONFIG_LAYOUT, JanuxConfigLayout

app = typer.Typer()


@app.callback(invoke_without_command=True)
def init(
    ctx: typer.Context,
    root: Path = typer.Option(
        ".",
        "--root",
        help="Folder in which the configuration tree is created.",
        file_okay=False,
        resolve_path=True,
    ),
    destination: Optional[Path] = typer.Option(
        None,
        "--destination",
        hidden=True,
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
    if destination is not None:
        # Former name of --root, kept for one release as a hidden alias.
        if ctx.get_parameter_source("root") is not ParameterSource.DEFAULT:
            raise typer.BadParameter("--destination is the former name of --root; give only --root.")
        typer.echo("Warning: --destination is deprecated and will be removed; use --root.", err=True)
        root = destination
    try:
        layout = JanuxConfigLayout(
            config_root=config_root, janux_root=janux_root, subdirectories=tuple(subdirectory)
        )
    except ValueError as error:
        raise typer.BadParameter(str(error)) from error
    request = JanuxInitRequest(destination=root, layout=layout)
    request = create_config_structure(request)
    typer.echo(f"Janux configuration initialized in: {request.config_root}")
