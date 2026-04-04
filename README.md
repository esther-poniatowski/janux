# Janux

[![Conda](https://img.shields.io/badge/conda-eresthanaconda--channel-blue)](docs/guide/installation.md)
[![Maintenance](https://img.shields.io/maintenance/yes/2026)]()
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/janux)](https://github.com/esther-poniatowski/janux/commits/main)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.12-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Automates project-scoped SSH connections across remote servers.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

### Motivation

Research and development workflows frequently involve transferring files and running
commands on remote servers. Managing SSH credentials, host configurations, and transfer
recipes across multiple projects and servers requires repetitive, error-prone setup.

### Advantages

- **Project-scoped credentials** — SSH keys, usernames, and host aliases are organized
  per project rather than scattered across `~/.ssh/config`.
- **Declarative connections** — host access and transfer workflows are defined in YAML
  and tracked in version control, eliminating ad-hoc scripts and manual `scp`/`rsync`
  commands.
- **Automated provisioning** — key generation, remote key deployment, and
  `~/.ssh/config` updates are handled through a single CLI.

---

## Features

- [ ] **Host management**: Define remote hosts through aliases with configurable
  connection parameters.
- [ ] **Credential management**: Generate, store, and deploy SSH keys per project,
  isolated from global SSH configuration. Manage multiple server identities from
  credential files.
- [ ] **Connection profiles**: Group hosts, credentials, and transfer rules into
  reusable profiles with password-free authentication.
- [ ] **Non-interactive scripting**: Launch remote commands without manual password
  entry or interactive prompts.
- [ ] **Transfer workflows**: Transfer files across servers with structured directory
  mappings, exclusion patterns, and dry-run support.

---

## Quick Start

Connect to a registered host:

```sh
janux connect myserver
```

Display version and platform diagnostics:

```sh
janux info
```

---

## Documentation

| Guide | Content |
| ----- | ------- |
| [Installation](docs/guide/installation.md) | Prerequisites, pip/conda/source setup |
| [Usage](docs/guide/usage.md) | Workflows and detailed examples |
| [CLI Reference](docs/guide/cli-reference.md) | Full command registry and options |
| [Configuration](docs/guide/configuration.md) | Host aliases, credentials, profiles |

Full API documentation and rendered guides are also available at
[esther-poniatowski.github.io/janux](https://esther-poniatowski.github.io/janux/).

---

## Contributing

Contribution guidelines are described in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Acknowledgments

### Authors

**Author**: @esther-poniatowski

For academic use, the GitHub "Cite this repository" feature generates citations in
various formats. The [citation metadata](CITATION.cff) file is also available.

---

## License

This project is licensed under the terms of the
[GNU General Public License v3.0](LICENSE).
