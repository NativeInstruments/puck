from puck.backend import echo_backend
from puck.parser import parse_requirement


def test_parse_req():
    expected = {
        'name': 'foo',
        'pinned_version': '1.2.3',
        'latest_version': 'foo',
        'source': None
    }
    assert parse_requirement(
        'foo==1.2.3',
        None,
        backend=echo_backend
    ) == expected


def test_parse_invalid_req():
    assert parse_requirement(
        'foo<1.2.3',
        None,
        backend=echo_backend
    ) is None
