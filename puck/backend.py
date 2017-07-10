from six.moves import xmlrpc_client

'''
Backends take a Python distribution release name and return the current version
present on PyPI. Test backends are provided for unit testing without hitting
the network.
'''

PYPI_URL = 'https://pypi.python.org/pypi'


def pypi_backend(release_name):
    """Actual PyPI backend. Uses an XMLRPC client to fetch release info"""
    pypi = xmlrpc_client.ServerProxy(PYPI_URL)
    return pypi.package_releases(release_name)[0]


def echo_backend(name):
    """Returns the given release name as the version"""
    return name


def high_version_backend(name):
    """Always returns '99.99.99' """
    return '99.99.99'
