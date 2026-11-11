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
janux init [-r|--root PATH] [--config-root PATH] [--janux-root NAME] [--subdirectory NAME]...
```

| Option          | Default | Description                                  |
| --------------- | ------- | -------------------------------------------- |
| `-r`, `--root`  | `JANUX_ROOT`, else `.` | Folder in which the configuration tree is created. |
| `--config-root` | `config/local` | Folder of the configuration, relative to the root. |
| `--janux-root`  | `janux` | Folder of Janux inside the configuration folder. |
| `--subdirectory` | `hosts`, `credentials`, `profiles` | Subdirectory to create in the folder of Janux; repeat the option for several. |

By default, the command creates `config/local/janux/` under the root, with
subdirectories `hosts/`, `credentials/`, and `profiles/`. Hosts, credentials and
profiles depend on one machine, so a project ignores `config/local/`. The options
place the tree elsewhere; a configuration folder outside the root is rejected.

The root is the folder given by `--root`, else the folder named by the environment variable
`JANUX_ROOT`, else the current folder. Janux has no configuration file, so it does not search the
ancestors of the current folder for one. A relative path is read from the current folder.

The command creates folders only. Existing folders and the files that they hold are preserved,
so the command can run again on an initialized project. A file that occupies the place of a
folder of the tree is never replaced: the command stops and names the file.

**Exit behavior:** prints the path of the created folder of Janux and exits with status 0.
A usage error, such as an unknown option or argument, a configuration folder outside the root,
or a file in place of a folder, exits with status 2.
