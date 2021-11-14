import pytest
from spacex_trello_api.trello_api import app
from requests_mock.mocker import Mocker
from spacex_trello_api.trello_api import TRELLO_KEY, TRELLO_TOKEN, TRELLO_TODO_LIST

@pytest.fixture
def client():
    app_test = app
    with app_test.test_client() as client:
        yield client

def test_about_flask_ok(client):
    rv = client.get('/about')
    assert b'This is SpaceX API Trello' in rv.data

def test_add_issue(requests_mock: Mocker, client):
    requests_mock.post(url="https://api.trello.com/1/cards",
                       headers={'key': TRELLO_KEY, 'token': TRELLO_TOKEN, 'idList': TRELLO_TODO_LIST,
                                'name': 'hola', 'desc': 'mundo'},
                       text='issue added'
                       )
    r = client.post('/add_issue/hola/mundo')
    assert r.data == bytes('issue added', 'utf-8')

def test_add_bug(requests_mock: Mocker, client):
    requests_mock.post(url="https://api.trello.com/1/cards",
                       headers={'key': TRELLO_KEY, 'token': TRELLO_TOKEN, 'idList': TRELLO_TODO_LIST,
                                'desc': 'dangerous'},
                       text='bug added'
                       )
    r = client.post('/add_bug/dangerous')
    assert r.data == bytes('bug added', 'utf-8')

def test_add_task(requests_mock: Mocker, client):
    requests_mock.post(url="https://api.trello.com/1/cards",
                       headers={'key': TRELLO_KEY, 'token': TRELLO_TOKEN, 'idList': TRELLO_TODO_LIST,
                                'name': 'hello'},
                       text='task added'
                       )
    r = client.post('/add_task/hello')
    assert r.data == bytes('task added', 'utf-8')
