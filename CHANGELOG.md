# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed

- `janux init` takes the folder in which it creates the configuration tree from `--root`,
  the option name shared by the tools of the workspace.

### Deprecated

- `janux init --destination` is a hidden alias of `--root`, kept for one release. It prints a
  warning that names `--root`, and it will be removed in the next release.
