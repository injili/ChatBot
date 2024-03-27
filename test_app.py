import pytest
from app import app
from app import get_completion

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_completion():
    # Test with a simple prompt
    prompt = "Tell me about cybersecurity."
    response = get_completion(prompt)
    assert isinstance(response, str)
    assert len(response) > 0

def test_get_bot_response(client):
    # Simulate a user request with a specific message
    user_input = "Hello, cyafe!"
    response = client.get(f"/get?msg={user_input}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response content is not empty
    assert response.data


def test_index_route(client):
    # Simulate a request to the root route
    response = client.get('/')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains expected content (e.g., template rendering)
    assert b'<!DOCTYPE html>' in response.data


def test_404_page(client):
    # Simulate a request to a non-existent route
    response = client.get('/nonexistent')

    # Check if the response status code is 404
    assert response.status_code == 404

    # Check if the response contains expected content (e.g., 404.html rendering)
    assert b'<!DOCTYPE html>' in response.data

if __name__ == "__main__":
    pytest.main()
