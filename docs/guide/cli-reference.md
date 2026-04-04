# CLI Reference

Complete command registry for the `janux` CLI.

The entry point is defined in `pyproject.toml` under `[project.scripts]` and
maps to `janux.cli:app`. The CLI can also be invoked as `python -m janux`.

## Global Options

| Option              | Description                          |
| ------------------- | ------------------------------------ |
| `--version` / `-v`  | Print the package version and exit.  |
| `--help`            | Show the help message and exit.      |

When invoked with no arguments, `janux` prints the help message.

## `info`

Print version and platform diagnostics.

```sh
janux info
```

**Arguments:** none.

**Output format:** single line containing the package name, version, operating
system, and Python version.

## `init`

Create the Janux configuration directory tree.

```sh
janux init [--destination PATH]
```

| Option          | Default | Description                                  |
| --------------- | ------- | -------------------------------------------- |
| `--destination` | `.`     | Target directory for the configuration tree. |

The command creates `config/janux/` under the destination, with
subdirectories `hosts/`, `credentials/`, and `profiles/`. Existing directories
are preserved.

**Exit behavior:** prints the path to the created configuration root.
