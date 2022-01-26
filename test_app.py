import os
import sys
import pytest
from app import app


client = app.test_client()

def test_hello():
    resp_index = client.get('/')

    assert resp_index.status_code == 302
    assert b'Redirecting...' in resp_index.data

    resp = client.get('/helloworld')
    assert resp.status_code == 200
    assert b'Hello Stranger' in resp.data

def test_hello_name():
    resp = client.get('/helloworld?name=')

    assert resp.status_code == 200
    assert b'Hello Stranger' in resp.data

    resp1 = client.get('helloworld?name=CharlotteEvelynNeumann')

    assert resp1.status_code == 200
    assert b'Hello Charlotte Evelyn Neumann' in resp1.data

def test_versionz(capsys):

    resp = client.get('/versionz')

    # read git hash in stdout 
    stdout = os.popen('git rev-parse origin/main').read()

    assert resp.status_code == 200
    assert resp.json['hash'] in stdout
    assert resp.json['project_name'] == "helloendocode"
    