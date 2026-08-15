import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_status():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200


def test_get_post_body():
    response = requests.get(f"{BASE_URL}/posts/1")

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/999999")

    assert response.status_code == 404


