import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():
    payload = {
        "title": "Мой тестовый пост",
        "body": "Тело тестового поста",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    assert "id" in data

