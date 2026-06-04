import pytest
from app.main import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_returns_json(client):
    res = client.get('/health')
    data = res.get_json()
    assert data['status'] == 'healthy'


def test_info_returns_version(client):
    res = client.get('/api/info')
    data = res.get_json()
    assert 'version' in data
