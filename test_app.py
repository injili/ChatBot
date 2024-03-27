import pytest
from app import app
from app import get_completion

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_completion():
    prompt = "Tell me about cybersecurity."
    response = get_completion(prompt)
    assert isinstance(response, str)
    assert len(response) > 0

def test_get_bot_response(client):
    user_input = "Hello, cyafe!"
    response = client.get(f"/get?msg={user_input}")
    assert response.status_code == 200
    assert response.data


def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data


def test_404_page(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'<!DOCTYPE html>' in response.data

if __name__ == "__main__":
    pytest.main()
