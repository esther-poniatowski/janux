# Configuration

## Directory Layout

Running `janux init` creates the following tree under the target directory:

```text
config/
  janux/
    hosts/          # Host alias definitions (planned)
    credentials/    # SSH key references (planned)
    profiles/       # Connection profiles (planned)
```

The `JanuxConfigLayout` dataclass in `janux.initialization.setup` defines the
directory names. Default values:

| Field            | Default                                  |
| ---------------- | ---------------------------------------- |
| `config_root`    | `config`                                 |
| `janux_root`     | `janux`                                  |
| `subdirectories` | `hosts`, `credentials`, `profiles`       |

## Configuration Files

No configuration file formats are implemented. The subdirectories created by
`init` are empty placeholders. Future versions will populate `hosts/`,
`credentials/`, and `profiles/` with YAML files parsed by the domain model
(`ConnectionSpec`, `HostConfig`).

## Third-Party Tool Configs

The repository stores tool configurations separately from Janux-specific
settings:

```text
config/
  tools/
    black.toml
    mypy.ini
    pylintrc.ini
    pylintrc_tests.ini
    pyrightconfig.json
    releaserc.toml
  dictionaries/
```

These files configure linters, formatters, type checkers, and release
automation. The `janux init` command does not create or modify the `config/tools/`
or `config/dictionaries/` directories.
