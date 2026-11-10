# TODO

Items are grouped by the condition that opens them.

## Needs of the project repositories

- [ ] **Replace the connection scripts of Multitask.** Multitask Context-Dependent Behavior connects to its servers through the shell scripts of `src/shell/etl/remote_access/`: `ssh_connection.sh` and `ssh_utils.sh` open the connection with credentials read from a file outside the repository, and `mount_data.sh` mounts the data of a server with sshfs. Janux implements only `init` and `info` today. The replacement needs the hosts, the credentials read from a file outside the repository, the profiles and `janux connect`, then the transfers with their maps of folders. Decide whether Janux offers a mount command, or leaves mounting to sshfs. The project keeps its configuration in `config/janux/`, and keeps the keys themselves outside the repository.

## Needs of the rule on parameters and settings

- [x] **Make the initialization customizable.** `janux init` exposes only `--destination`, whereas the dataclass `JanuxConfigLayout` declares `config_root`, `janux_root` and `subdirectories`. `init` must let each project choose these values, through options of the command or a file of the project. Done on 2026-11-10: `--config-root`, `--janux-root` and `--subdirectory`.
- [x] **Keep the settings of a machine out of the versioned configuration.** The [rule on project repositories](https://github.com/esther-poniatowski/geonexus/blob/main/docs/rules/project-repositories.md) places hosts, credentials and connection profiles, which depend on one machine, in `config/local/`, which Git ignores. `janux init` creates them under `config/janux/`. Its default location must become `config/local/janux/`, once the initialization is customizable. Done on 2026-11-10.
