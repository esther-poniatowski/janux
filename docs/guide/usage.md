# Usage

Janux automates SSH connections and file transfers across remote servers,
organized by project. Hosts, credentials, and transfer workflows are defined
declaratively in YAML.

For the full command registry, refer to [CLI Reference](cli-reference.md). For
host and credential settings, refer to [Configuration](configuration.md).

## Registering a Remote Host

Define a host alias with connection parameters:

```sh
janux host add myserver --hostname 192.168.1.100 --user admin --port 22
```

Host aliases abstract away IP addresses and connection details, allowing
subsequent commands to reference hosts by name.

## Connecting to a Host

Open an SSH session to a registered host:

```sh
janux connect myserver
```

## Managing SSH Credentials

Generate a new SSH key pair scoped to the current project:

```sh
janux key generate --name project-key
```

Deploy a public key to a remote host:

```sh
janux key deploy project-key --host myserver
```

## Transferring Files

Define a transfer recipe in the project configuration and execute it by name:

```sh
janux transfer run sync-data --host myserver
```

Transfer recipes support path mapping, exclusion patterns, and dry-run
inspection:

```sh
janux transfer run sync-data --host myserver --dry-run
```

## Listing Resources

List all registered hosts:

```sh
janux host list
```

List all available credentials:

```sh
janux key list
```

## Next Steps

- [CLI Reference](cli-reference.md) — Full command registry and options.
- [Configuration](configuration.md) — Host aliases, credentials, profiles.
