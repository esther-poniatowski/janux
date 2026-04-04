# Usage

Janux scaffolds a project-scoped configuration directory for SSH connections.
Additional features (host registration, key management, file transfers) are
planned but not yet implemented.

For the full command registry, refer to [CLI Reference](cli-reference.md). For
the directory layout created by `init`, refer to
[Configuration](configuration.md).

## Initializing a Project

The `init` command creates the Janux configuration directory tree under the
current working directory:

```sh
janux init
```

The resulting layout:

```text
config/janux/
  hosts/
  credentials/
  profiles/
```

A different root can be specified with `--destination`:

```sh
janux init --destination ~/projects/my-project
```

The command is idempotent -- running `init` again leaves existing directories
intact.

## Displaying Diagnostics

The `info` command prints the installed version and platform details:

```sh
janux info
```

Example output:

```text
janux 0.0.0 | Platform: Darwin Python 3.12.0
```

## Checking the Version

```sh
janux --version
```

Prints the package version string and exits.

## Planned Features

The following capabilities are defined in the domain model but have no CLI
commands yet:

- **Host registration** -- add, list, and remove remote host aliases.
- **SSH key management** -- generate, deploy, and list SSH key pairs.
- **Connection** -- open interactive SSH sessions to registered hosts.
- **File transfers** -- execute declarative transfer recipes.

## Next Steps

- [CLI Reference](cli-reference.md) -- full command registry and options.
- [Configuration](configuration.md) -- directory layout and file formats.
