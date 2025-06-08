# Janux

[![Conda](https://img.shields.io/badge/conda-eresthanaconda--channel-blue)](#installation)
[![Maintenance](https://img.shields.io/maintenance/yes/2025)]()
[![Last Commit](https://img.shields.io/github/last-commit/esther-poniatowski/janux)](https://github.com/esther-poniatowski/janux/commits/main)
[![Python](https://img.shields.io/badge/python-supported-blue)](https://www.python.org/)
[![License: GPL](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/GPL-3.0)

Remote access manager for automating project-specific server connections via reproducible and scoped
SSH configurations.

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

Complex projects often involve executing distributed workflows across multiple remote servers and
transferring data across them. This requires managing heterogeneous SSH configurations, credentials,
and file transfer schemes.

In standard practice, connections are manually configured on a designated controller machine, with
SSH keys and settings stored globally in user or system locations. This approach is not scalable in
collaborative or ephemeral computing environments, where multiple users and temporary controller
machines must be provisioned. It results in repetitive setup procedures, unmanaged key
proliferation, and residual configuration artifacts persisting after project completion.

### Advantages

This tool introduces a remote access management system for automated, reproducible, and
project-scoped server orchestration.

It provides the following benefits:

- **Isolated configuration management**: Encapsulates credentials and host aliases at the project
  level to avoid contamination of global SSH settings.
- **Simplified access and identity handling**: Supports alias-based SSH connections and secure,
  password-less authentication across multiple server identities.
- **Automated setup and teardown**: Facilitates fast, consistent provisioning and cleanup of
  temporary controller environments through pre-defined procedures.
- **Reproducible execution and transfer workflows**: Automates task deployment and file
synchronization across servers via declarative, version-controlled access specifications and
directory mappings.

---

## Features

- [ ] **Identity-based connection management**: Manages multiple server identities from credential
  files.
- [ ] **Alias-based host access**: Simplifies SSH connections using short labels.
- [ ] **Non-interactive scripting support**: Launches remote commands without manual password entry
  or prompts.
- [ ] **Project-specific SSH key management**: Isolates key storage to prevent global pollution of
  SSH configurations.
- [ ] **Secure file transfers**: Transfers files across servers with structured directory mappings.

---

## Installation

To install the package and its dependencies, use one of the following methods:

### Using Pip Installs Packages

Install the package from the GitHub repository URL via `pip`:

```bash
pip install git+https://github.com/esther-poniatowski/janux.git
```

### Using Conda

Install the package from the private channel eresthanaconda:

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

To display the list of available commands and options:

```sh
janux --help
```

### Programmatic Usage

To use the package programmatically in Python:

```python
import janux
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
