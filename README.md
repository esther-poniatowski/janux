# Janux

[![Conda](https://img.shields.io/badge/conda-eresthanaconda--channel-blue)](#installation)
[![Maintenance](https://img.shields.io/maintenance/yes/2026)]()
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/janux)](https://github.com/esther-poniatowski/janux/commits/main)
[![Python](https://img.shields.io/badge/python-supported-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Remote access manager that automates SSH connections scoped to each project across multiple servers.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Support](#support)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

### Motivation

Complex projects often run distributed workflows across multiple remote servers and transfer data
between them, requiring heterogeneous SSH configurations, credentials, and file transfer schemes.

Standard practice stores SSH keys and settings globally on a designated controller machine.
That approach does not scale in collaborative or ephemeral environments: setup is repetitive,
keys proliferate without control, and residual configuration persists after project completion.

### Advantages

Janux automates SSH access at the project level:

- **Isolated credentials**: Keeps credentials and host aliases scoped to the project, avoiding
  contaminating global SSH settings.
- **Access through aliases**: Connects to servers through short labels with secure
  authentication (without passwords) across multiple identities.
- **Automated provisioning**: Sets up and tears down temporary controller environments through
  predefined procedures.
- **Declarative transfer workflows**: Deploys tasks and synchronizes files across servers via
  access specifications tracked in version control and directory mappings.

---

## Features

- [ ] **Connections by identity**: Manages multiple server identities from credential files.
- [ ] **Host access through aliases**: Simplifies SSH connections using short labels.
- [ ] **Non-interactive scripting support**: Launches remote commands without manual password entry
  or prompts.
- [ ] **SSH keys scoped to the project**: Isolates key storage to prevent global pollution of
  SSH configurations.
- [ ] **Secure file transfers**: Transfers files across servers with structured directory mappings.

---

## Installation

### Using pip

Install from the GitHub repository:

```bash
pip install git+https://github.com/esther-poniatowski/janux.git
```

### Using conda

Install from the eresthanaconda channel:

```bash
conda install janux -c eresthanaconda
```

### From Source

1. Clone the repository:

      ```bash
      git clone https://github.com/esther-poniatowski/janux.git
      ```

2. Create a dedicated virtual environment:

      ```bash
      cd janux
      conda env create -f environment.yml
      ```

---

## Usage

### Command Line Interface (CLI)

Initialize the Janux configuration structure for a project:

```sh
janux init --destination ./my_project
```

The `init` command creates a `config/janux/` directory with templates for SSH host aliases,
credentials, and connection profiles.

Display version and platform diagnostics:

```sh
janux info
```

### Programmatic Usage

```python
from janux.initialization import create_config_structure

# Initialize config structure programmatically
create_config_structure(destination="./my_project")
```

---

## Configuration

### Environment Variables

|Variable|Description|Default|Required|
|---|---|---|---|
|`VAR_1`|Description 1|None|Yes|
|`VAR_2`|Description 2|`false`|No|

### Configuration File

Configuration options are specified in YAML files located in the `config/` directory.

The canonical configuration schema is provided in [`config/default.yaml`](config/default.yaml).

```yaml
var_1: value1
var_2: value2
```

---

## Documentation

- [User Guide](https://esther-poniatowski.github.io/janux/guide/)
- [API Documentation](https://esther-poniatowski.github.io/janux/api/)

> [!NOTE]
> Documentation can also be browsed locally from the [`docs/`](docs/) directory.

## Support

**Issues**: [GitHub Issues](https://github.com/esther-poniatowski/janux/issues)

**Email**: `{{ contact@example.com }}`

---

## Contributing

Please refer to the [contribution guidelines](CONTRIBUTING.md).

---

## Acknowledgments

### Authors & Contributors

**Author**: @esther-poniatowski

**Contact**: `{{ contact@example.com }}`

For academic use, please cite using the GitHub "Cite this repository" feature to
generate a citation in various formats.

Alternatively, refer to the [citation metadata](CITATION.cff).

### Third-Party Dependencies

- **[Library A](link)** - Purpose
- **[Library B](link)** - Purpose

---

## License

This project is licensed under the terms of the [GNU General Public License v3.0](LICENSE).
