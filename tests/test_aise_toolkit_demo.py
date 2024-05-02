from click.testing import CliRunner
from aise_toolkit_demo.cli import cli

def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")

def test_first_command():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["command", "example", "-o", "option"])
        assert result.exit_code == 0
        assert result.output == "Here is some output\n"
