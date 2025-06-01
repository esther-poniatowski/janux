<!---
ARCHIVED
- Date: 2025-06-01
- Reason: New version adhering to template in "keystone/README.md".
-->
# Janux

Utility for automating secure server connections.

## Features

- [ ] **Identity-based connection management**: Manages multiple server identities from credential
  files.
- [ ] **Alias-based host access**: Simplifies SSH connections using short labels.
- [ ] **Non-interactive scripting support**: Launches remote commands without manual password entry
  or prompts.
- [ ] **Project-specific SSH key management**: Isolates key storage to prevent global pollution of
  SSH configurations.
- [ ] **Secure file transfers**: Transfers files across servers with structured directory mappings.

## Installation

### Pre-requisites

The following usage is recommended:

- **Project-specific usage:** Integrate `janux` into a specific project, where multiple server
  identities or isolated configurations are required, rather than using it as a global system tool.
- **Virtual environment**: Isolate `janux` dependencies from the global Python installation.

### As a Command Line Tool (Recommended)

1. Install the `janux` utility in the virtual environment of the project:

    ```bash
    pip install janux
    ```

2. Verify installation:

    ```sh
    janux --help
    ```

    Expected output should display usage options and command-line arguments.

3. Initialize the default structure for the utility in the project directory:

    ```sh
    janux init
    ```

    This command will create a `config/janux` directory (if it does not exist) containing template
    files and folders:

    - `janux.conf` file: for `janux` settings,
    - `ssh_spec.ini` file: for specifying server aliases and identities,
    - `transfer_map` file: for defining a file transfer operation,
    - `ssh_keys/` folder: for isolated key storage.

### As a Standalone Dependency

This approach is only relevant to:

- Use `janux` as a fully accessible and editable package within the main project during development.
- Synchronize with updates via `git pull` or `git subtree pull`.

1. Download the repository within a dedicated directory in the project (e.g. include), via one of
   the following options:

   - Git Submodule (if integrated with a larger project):

     ```sh
     git submodule add https://github.com/esther-poniatowski/janux.git include/janux
     ```

   - Git Subtree (to manage it independently):

     ```sh
     git subtree add --prefix include/janux https://github.com/esther-poniatowski/janux.git main
     ```

2. Install dependencies, via one of the following options:

    - Using pip (requires `toml-to-requirements`):

    ```sh
    toml-to-req --toml-file include/janux/pyproject.toml --requirements-file include/janux/requirements.txt
    pip install -r include/janux/requirements.txt
    ```

    - Using conda (replace `myenv` by the name of the virtual environment):

    ```sh
    conda env update --name myenv --file include/janux/environment.yml
    ```

3. Initialize the configuration:

    ```sh
    python include/janux/main.py init
    ```

4. Optionally, to import `janux` modules programmatically in the project's code, two options are
   available:

    - Using pip to install `janux` in editable mode:

    ```sh
    pip install -e include/janux
    ```

    - Using conda, add the `src` directory to Python's `site-packages` (replace `myenv` by the name
      of the virtual environment):

    ```sh
    conda activate myenv
    echo "$(pwd)/include/janux/src" > $(python -c "import site; print(site.getsitepackages()[0])")/janux.pth
    ```

    This command locates the `site-packages` directory of the activated Conda environment (typically
    `/path/to/miniconda3/envs/myenv/lib/pythonX.Y/site-packages`), and creates a `janux.pth` file
    containing the absolute path to `janux/src`. This directory will be automatically added to the
    `sys.path` variable upon environment activation.

After one of the above operation is performed, `janux` is available directly for imports (see
section [Within a Script](#within-a-script)). Any modification in `janux`code is applied immediately
without reinstalling.

## Configuration File

Settings for the `janux` utility are specified in a central configuration file named `janux.conf`,
located in the user's project directory.

Standard locations of the configuration file, by precedence:

1. Project's root directory: `project_name/`
2. Project's configuration directory: `project_name/config/`
3. janux directory within configurations: `project_name/config/janux/`

## Usage

### Specifying Server Identities

Server identities are centralized in a configuration file located in the user's project directory.
By default, this file is generated under the name `ssh_spec.ini` in the configuration folder
`config/janux/`. Custom locations and file names can be specified by the setting `spec_path` in
`janux.conf`.

Each server is specified with an alias and connection information, following the standard syntax of
SSH configuration files:

```ini
[server_alias]
host = 192.168.1.10
user = admin
identity_file = path/to/keys/alias_key
```

Project-specific servers can be added by two approaches:

- Statically, by editing the `janux.conf` configuration file:
- Dynamically, from the command line.

Add a host with an alias:

```sh
TODO: Complete the code.
```

### Setting up SSH Keys

Project-specific SSH keys are generated automatically from the configuration file:

```sh
janux generate-keys
```

By default, keys are stored locally under `config/ssh_keys/`. They can be stored in a custom
location using the option `--key_path`.

> [NOTE] To isolate project-specific configurations from the global SSH configuration, keys can be
> stored in a local project directory, such as `config/ssh_keys`. This local storage prevents
> unnecessary key persistence on the host machine when the project is removed. This approach is
> particularly relevant for short-term projects that need to be run from various clones, which all
> connect to the same remote servers.

### Connecting to a Remote Server

Once SSH keys are configured, connections are automated for both command line and non-interactive
scripting.

The utility automatically performs the following connection steps:

1. Retrieving the connection information from the configuration file.
2. Adding the appropriate SSH key to the SSH agent.
3. Executing the SSH command.

#### From the command line

Connect to a host via its alias:

```sh
TODO: Complete the code
```

#### Within a Script

Import the `janux` utility:

 ```python
 from janux.connection import SSHConnection
 from janux.key_management import KeyManager
 from janux.configuration import ConfigLoader
 ```

### Transferring files

Files can be transferred and organized via declarative tree mappings.

1. Define a file transfer map following the template in `transfer_map.yml`, specifying the source
   and destination tree structure (paths, file names) and rules. Example: TODO: Give example.

2. TODO: Detail the procedure.

## Repository Structure

```tree
janux/
├── config/
│   ├── janux.conf                   # Template file for janux settings
│   ├── ssh_spec.ini                 # Template file for server aliases and identities
│   └── transfer_map.yml             # Template for file transfer rules
├── src/
│   └── janux/
│       ├── __init__.py
│       ├── __main__.py              # Main package entry point for CLI calls
│       ├── cli/                     # CLI subcommands
│       ├── configuration/           # Load/parse/validate configurations and mappings
│       ├── connection/              # SSH connection logic, authentication, error handling
│       ├── key_management/          # SSH key generation, encryption, storage
│       ├── transfer/                # File transfer logic across servers
│       └── utils/                   # Shared utility functions, centralized logging, validation...
├── tests/                           # Tests for the full package
├── docs/                            # API documentation
├── scripts/                         # Auxiliary scripts for environment setup and installation
├── environment.yml                  # Python dependencies for conda
├── pyproject.toml                   # Setup script for pip installation
├── .gitignore
├── README.md
└── LICENSE
```

## License

This project is under [GPL License].
