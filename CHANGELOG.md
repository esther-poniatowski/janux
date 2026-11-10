# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed

- `-v`/`--version` prints the version without a command. The option was not eager, so the command
  line stopped with "Missing command" and status 2.

### Changed

- `janux init` takes the folder in which it creates the configuration tree from `-r`/`--root`,
  the option name shared by the tools of the workspace, else from the environment variable
  `JANUX_ROOT`, else from the current folder.
- `janux init` stops with status 2 and names the file when a file occupies the place of a folder
  of the tree, instead of failing with a traceback.
- `janux init` is a plain command: its usage no longer announces subcommands.

### Removed

- `janux init --destination`, the former name of `--root`. The option is rejected.
