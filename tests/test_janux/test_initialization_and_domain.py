from pathlib import Path

import pytest

from janux.domain import ConnectionSpec, HostConfig
from janux.initialization import JanuxInitRequest, create_config_structure
from janux.initialization.setup import JanuxConfigLayout


def test_create_config_structure_accepts_missing_destination(tmp_path: Path) -> None:
    request = create_config_structure(tmp_path / "new-project")

    assert isinstance(request, JanuxInitRequest)
    assert request.config_root == tmp_path / "new-project" / "config" / "local" / "janux"
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


def test_layout_places_the_tree_where_the_request_asks(tmp_path: Path) -> None:
    layout = JanuxConfigLayout(config_root="settings", janux_root="remote", subdirectories=("hosts",))
    request = create_config_structure(JanuxInitRequest(destination=tmp_path, layout=layout))

    assert request.config_root == tmp_path / "settings" / "remote"
    assert [path.name for path in request.config_root.iterdir()] == ["hosts"]


def test_layout_rejects_a_root_outside_the_destination() -> None:
    with pytest.raises(ValueError, match="relative path"):
        JanuxConfigLayout(config_root="../elsewhere")


def test_init_command_takes_the_layout_from_its_options(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli.init import app

    result = CliRunner().invoke(app, ["--root", str(tmp_path), "--config-root", "config",
                                      "--janux-root", "janux", "--subdirectory", "hosts",
                                      "--subdirectory", "profiles"])
    assert result.exit_code == 0, result.output
    created = sorted(path.name for path in (tmp_path / "config" / "janux").iterdir())
    assert created == ["hosts", "profiles"]
    rejected = CliRunner().invoke(app, ["--root", str(tmp_path), "--config-root", "/abs"])
    assert rejected.exit_code != 0


def test_init_command_creates_the_tree_under_the_root(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli.init import app

    result = CliRunner().invoke(app, ["--root", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "config" / "local" / "janux" / "hosts").is_dir()
    assert "deprecated" not in result.stderr


def test_init_command_rejects_the_retired_destination_option(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli.init import app

    result = CliRunner().invoke(app, ["--destination", str(tmp_path)])
    assert result.exit_code == 2
    assert not (tmp_path / "config").exists()


def test_init_command_takes_the_root_from_the_environment(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli.init import app

    result = CliRunner().invoke(app, [], env={"JANUX_ROOT": str(tmp_path)})
    assert result.exit_code == 0, result.output
    assert (tmp_path / "config" / "local" / "janux" / "hosts").is_dir()
    explicit = tmp_path / "explicit"
    result = CliRunner().invoke(app, ["-r", str(explicit)], env={"JANUX_ROOT": str(tmp_path)})
    assert result.exit_code == 0, result.output
    assert (explicit / "config" / "local" / "janux" / "hosts").is_dir()


def test_init_command_is_idempotent_and_keeps_existing_files(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli.init import app

    assert CliRunner().invoke(app, ["--root", str(tmp_path)]).exit_code == 0
    note = tmp_path / "config" / "local" / "janux" / "hosts" / "lab.yml"
    note.write_text("host: example.org\n")
    result = CliRunner().invoke(app, ["--root", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert note.read_text() == "host: example.org\n"


def test_init_command_refuses_a_file_in_place_of_a_folder(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli.init import app

    blocking = tmp_path / "config" / "local" / "janux" / "profiles"
    blocking.parent.mkdir(parents=True)
    blocking.write_text("kept")
    result = CliRunner().invoke(app, ["--root", str(tmp_path)])
    assert result.exit_code == 2
    assert str(blocking) in result.stderr
    assert blocking.read_text() == "kept"
    assert not (tmp_path / "config" / "local" / "janux" / "hosts").exists()


def test_init_command_rejects_a_trailing_token(tmp_path: Path) -> None:
    from typer.testing import CliRunner

    from janux.cli import app

    result = CliRunner().invoke(app, ["init", "--root", str(tmp_path), "extra"])
    assert result.exit_code == 2
    assert not (tmp_path / "config").exists()
