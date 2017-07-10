from click.testing import CliRunner
from puck.cmd import check


def test_req():
    runner = CliRunner()
    result = runner.invoke(check, ['-t', '-f', 'testdata/requirements.txt'])
    assert result.exit_code == 0
    assert 'pytest-cov' in result.output


def test_setup_py():
    runner = CliRunner()
    result = runner.invoke(check, ['-t', '-s', 'testdata/setup.py'])
    assert result.exit_code == 0
    assert 'pytest-cov' in result.output


def test_json_output():
    runner = CliRunner()
    result = runner.invoke(
        check,
        ['-t', '-s', 'testdata/setup.py', '-o', 'json']
    )

    assert result.exit_code == 0
    assert '"source": "testdata/setup.py"' in result.output
    assert '"name": "pytest-cov"' in result.output
    assert '"pinned_version": "2.4.0"' in result.output
