import requests

def test_users_api():

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200


def test_user_count():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    assert len(data) > 0

def test_name_exists():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    assert data[0]["name"] is not None

def test_email_exists():

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    assert data[0]["email"] is not None