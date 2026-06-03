import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'running' in res.data

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert b'healthy' in res.data

def test_info(client):
    res = client.get('/api/info')
    assert res.status_code == 200
    assert b'python-webapp-cicd-openshift' in res.data
