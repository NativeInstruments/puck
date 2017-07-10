import sys

from puck.backend import (PYPI_URL, echo_backend, high_version_backend,
                          pypi_backend)
from six import MovedModule, add_move

import pytest

add_move(MovedModule('mock', 'mock', 'unittest.mock'))  # isort:skip
from six.moves import mock  # noqa isort:skip


def test_high_version_backend():
    assert high_version_backend('foo') == '99.99.99'


def test_echo_backend():
    assert echo_backend('foo') == 'foo'


@pytest.mark.skipif(
    sys.version_info < (3, 3),
    reason="requires python3.3"
)
@mock.patch('xmlrpc.client.ServerProxy')
def test_pypi_backend_py3(server_mock):
    expected = None
    pypi_mock = server_mock.return_value
    pypi_mock.package_releases.return_value = [expected]

    return_val = pypi_backend('foo')

    server_mock.assert_called_with(PYPI_URL)
    pypi_mock.package_releases.assert_called_once()

    assert return_val == expected


@pytest.mark.skipif(
    sys.version_info >= (3, 0),
    reason="2.7 xmlrpc compatibility"
)
@mock.patch('xmlrpclib.ServerProxy')
def test_pypi_backend_py2(server_mock):
    expected = None
    pypi_mock = server_mock.return_value
    pypi_mock.package_releases.return_value = [expected]

    return_val = pypi_backend('foo')

    server_mock.assert_called_with(PYPI_URL)
    pypi_mock.package_releases.assert_called_once()

    assert return_val == expected
