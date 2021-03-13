# Example taken from:
# http://flask.pocoo.org/docs/1.0/testing/
# and suitably modified.
import os
import tempfile

import pytest

from web import app, db

@pytest.fixture
def client():
    print('adsfafd')
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    print('asdfasdf')
    app.config['FLASK_ENV'] = 'test'
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Kanban Board' in rv.data
