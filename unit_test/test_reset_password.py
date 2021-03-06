import os
import tempfile
from flask import url_for, request
import pytest
import jwt, os, json
from datetime import datetime, timedelta

from web import app, db

"""Mocking endpoints for testing"""
def login(client, redirect, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=redirect)

def signup(client, username, email, password, password2):
    return client.post('/signup', data=dict(
        username=username,
        email=email,
        password=password,
        password2=password2
    ))

def reset(client, email):
    return client.post('/reset', data=dict(
        email=email
    ), follow_redirects=True)

def reset_email_token_mock(client, username, email):
    # generate token and return it
    now = str(datetime.now())
    encoded_jwt = jwt.encode({"email": email, "datetime": now}, os.getenv('SECRET_KEY'), algorithm="HS256")
    return encoded_jwt

def reset_token(client, token, new_password, new_password2):
    return client.post('/reset/token/'+str(token), data=dict(
        new_password=new_password,
        new_password2=new_password2
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['FLASK_ENV'] = 'test'
    client = app.test_client()

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_resetting_password(client):
    """Testing trying to reset password"""
    user1 = signup(client, 'username', 'sample-1@todo.com', 'asdfasdf', 'asdfasdf')
    reset_ = reset(client, 'sample-1@todo.com')
    assert (b'Email with instructions to reset your password was sent!' in reset_.data)

def test_resetting_password_with_invalid_email(client):
    """Testing reseting password with invalid email"""
    user1 = signup(client, 'username', 'sample-1@todo.com', 'asdfasdf', 'asdfasdf')
    reset_ = reset(client, 'sample-2@todo.com')
    # we should see the same thing. We are showing the same messages so it doesn't allow user enumeration
    # through this page
    assert (b'Email with instructions to reset your password was sent!' in reset_.data)

def test_updating_password_with_invalid_token(client):
    """Testing trying to update password with invalid JWT"""
    user1 = signup(client, 'username', 'sample-1@todo.com', 'asdfasdf', 'asdfasdf')
    reset_ = reset(client, 'sample-2@todo.com')
    reset_token_ = reset_token(client, 'wrong-token', 'asdfasdf1', 'asdfasdf1')
    # trying to reset password with wrong token
    assert (b'Invalid token' in reset_token_.data)

def test_updating_password_without_saving_token_on_db(client):
    """Testing reset password with token that was not saved on DB.
    Token is being generated by our mock function (since originally it should only be sent
    to the user email)
    """
    user1 = signup(client, 'username', 'sample-1@todo.com', 'asdfasdf', 'asdfasdf')
    reset_token_ = reset_email_token_mock(client, 'username', 'sample-2@todo.com')
    update_password = reset_token(client, reset_token_, 'asdfasdf1', 'asdfasdf1')
    # trying to reset password with email mock and without saving token on DB
    assert (b'Invalid token' in update_password.data)