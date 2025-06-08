"""
janux.cli.init
==============

Initialize Janux configuration structure

Functions
---------
"""

import typer

from janux.initialization import create_config_structure

app = typer.Typer()

@app.command()
def init(destination: str = typer.Option(".", help="Target directory for Janux configuration.")):
    """
    Initializes the default structure for Janux in the specified destination.
    """
    create_config_structure(destination)
    typer.echo(f"Janux configuration initialized in: {destination}/config/janux")
