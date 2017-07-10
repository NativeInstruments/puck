import json

import click


"""An output function takes a set of entries returned by the parser and
outputs them in a certain way."""


def default_output(entries):
    """prints entries to stdout"""
    for entry in entries:
        click.echo("{} (pinned: {}, latest: {}) from '{}'".format(
            entry['name'],
            entry['pinned_version'],
            entry['latest_version'],
            entry['source'],
        ))


def json_output(entries):
    """prints entries as json to stdout"""
    click.echo(json.dumps(entries))


output_fn = {
    'default': default_output,
    'json': json_output
}
