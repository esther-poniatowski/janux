from pathlib import Path

import pytest

from janux.domain import ConnectionSpec, HostConfig
from janux.initialization import JanuxInitRequest, create_config_structure


def test_create_config_structure_accepts_missing_destination(tmp_path: Path) -> None:
    request = create_config_structure(tmp_path / "new-project")

    assert isinstance(request, JanuxInitRequest)
    assert request.config_root == tmp_path / "new-project" / "config" / "janux"
    assert request.config_root.is_dir()
    assert (request.config_root / "hosts").is_dir()
    assert (request.config_root / "credentials").is_dir()
    assert (request.config_root / "profiles").is_dir()


def test_init_request_rejects_file_destination(tmp_path: Path) -> None:
    target = tmp_path / "config.txt"
    target.write_text("not a directory")

    with pytest.raises(ValueError, match="directory path"):
        JanuxInitRequest(destination=target)


def test_connection_spec_normalizes_and_validates() -> None:
    spec = ConnectionSpec(
        host=" example.org ",
        user=" deploy ",
        identity_file=Path("~/id_ed25519"),
    )

    assert spec.host == "example.org"
    assert spec.user == "deploy"
    assert spec.identity_file == Path("~/id_ed25519").expanduser()

    with pytest.raises(ValueError, match="host must not be empty"):
        ConnectionSpec(host=" ", user="deploy")

    with pytest.raises(ValueError, match="port must be between 1 and 65535"):
        ConnectionSpec(host="example.org", user="deploy", port=0)


def test_host_config_rejects_empty_alias() -> None:
    with pytest.raises(ValueError, match="alias must not be empty"):
        HostConfig(alias=" ", connection=ConnectionSpec(host="example.org", user="deploy"))
