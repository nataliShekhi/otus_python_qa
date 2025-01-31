import pytest
import requests


def test_api_jsonplaceholder():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert response.status_code == 200
    assert "userId" in response.text


@pytest.mark.parametrize("number", [1, 25, 50, 100])
def test_api_jsonplaceholder_posts(number):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{number}")
    result = response.json()
    assert response.status_code == 200
    assert result["id"] == number


def test_api_jsonplaceholder_number_of_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    number_of_users = 10
    result = response.json()
    assert response.status_code == 200
    assert number_of_users == len(result)


def get_number_of_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    result = response.json()
    return len(result)


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_api_jsonplaceholder_by_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    result = response.json()
    assert response.status_code == 200
    assert result["id"] == user_id


def test_api_jsonplaceholder_photos():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    max_number_of_photos = 5000
    result = response.json()
    assert response.status_code == 200
    assert len(result) == max_number_of_photos
    assert "id" in response.text
    assert "url" in response.text
