# TODO

Items are grouped by the condition that opens them.

## Needs of the project repositories

- [ ] **Replace the connection scripts of Multitask.** Multitask Context-Dependent Behavior connects to its servers through the shell scripts of `src/shell/etl/remote_access/`: `ssh_connection.sh` and `ssh_utils.sh` open the connection with credentials read from a file outside the repository, and `mount_data.sh` mounts the data of a server with sshfs. Janux implements only `init` and `info` today. The replacement needs the hosts, the credentials read from a file outside the repository, the profiles and `janux connect`, then the transfers with their maps of folders. Decide whether Janux offers a mount command, or leaves mounting to sshfs. The project keeps its configuration in `config/janux/`, and keeps the keys themselves outside the repository.
