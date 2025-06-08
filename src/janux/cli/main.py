"""
janux.cli.main
==============

Main entry point for the Janux Command Line Interface.


See Also
--------
typer.Typer
    Main class for building command line interfaces.
"""
import typer

cli = typer.Typer(help="Janux CLI for automated project-specific remote server connections.",
                  no_args_is_help=True)


if __name__ == "__main__":
    cli()
