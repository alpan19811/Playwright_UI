from http.client import responses

import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def new_post():
    return {
        "title": "Мой тестовый пост",
        "body": "Тело тестового поста",
        "userId": 1
    }


@pytest.mark.api
@pytest.mark.smoke
def test_get_post(base_url):
    response = requests.get(f"{base_url}/posts/1")

    assert response.status_code == 200


@pytest.mark.api
@pytest.mark.regression
def test_get_post_body(base_url):
    response = requests.get(f"{base_url}/posts/1")

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


@pytest.mark.api
@pytest.mark.regression
def test_create_post(base_url, new_post):
    response = requests.post(f"{base_url}/posts", json=new_post)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == new_post['title']
    assert data['body'] == new_post['body']
    assert data["userId"] == new_post["userId"]
    assert "id" in data


@pytest.mark.api
@pytest.mark.smoke
def test_get_post_not_found(base_url):
    response = requests.get(f"{base_url}/posts/999999")

    assert response.status_code == 404