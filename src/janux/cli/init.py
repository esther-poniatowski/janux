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

import typer

from janux.initialization import JanuxInitRequest, create_config_structure
from janux.initialization.setup import DEFAULT_CONFIG_LAYOUT, JanuxConfigLayout

app = typer.Typer()


@app.callback(invoke_without_command=True)
def init(
    destination: Path = typer.Option(
        ".",
        help="Target directory for Janux configuration.",
        file_okay=False,
        resolve_path=True,
    ),
    config_root: str = typer.Option(
        DEFAULT_CONFIG_LAYOUT.config_root,
        help="Folder of the configuration, relative to the destination.",
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
    """Initialize the structure for Janux in the specified destination."""
    try:
        layout = JanuxConfigLayout(
            config_root=config_root, janux_root=janux_root, subdirectories=tuple(subdirectory)
        )
    except ValueError as error:
        raise typer.BadParameter(str(error)) from error
    request = JanuxInitRequest(destination=destination, layout=layout)
    request = create_config_structure(request)
    typer.echo(f"Janux configuration initialized in: {request.config_root}")
