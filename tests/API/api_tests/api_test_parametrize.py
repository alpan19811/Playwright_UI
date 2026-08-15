import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

class TestUsersApi:
# Задание 1: GET /users/{id} для существующих пользователей
    @pytest.mark.api
    @pytest.mark.parametrize("user_id", [1, 5, 10])
    def test_get_existing_user(self, base_url, user_id):
        response = requests.get(f"{base_url}/users/{user_id}")

        assert response.status_code == 200

        data = response.json()
        assert data["id"] == user_id
        assert "username" in data


    # Задание 2: GET /users/{id} с разными статусами
    @pytest.mark.api
    @pytest.mark.parametrize(
        "user_id, expected_status",
        [
            (1, 200),  # <-- исправлено 100 на 200
            (10, 200),
            (999999, 404),
        ],
    )
    def test_get_user_status(self, base_url, user_id, expected_status):
        response = requests.get(f"{base_url}/users/{user_id}")

        assert response.status_code == expected_status


    # Задание 3: POST /users с разными данными
    @pytest.mark.api
    @pytest.mark.parametrize(
        "payload",
        [
            {
                "name": "Пользователь 1",
                "username": "user1",
                "email": "user1@example.com",
            },
            {
                "name": "Пользователь 2",
                "username": "user2",
                "email": "user2@example.com",
            },
            {
                "name": "",
                "username": "user3",
                "email": "user3@example.com",
            },
        ],
        ids=[
            "User 1",
            "User 2",
            "User with empty name",
        ],
    )
    def test_create_user(self, base_url, payload):
        response = requests.post(f"{base_url}/users", json=payload)

        assert response.status_code == 201

        data = response.json()

        assert data["name"] == payload["name"]
        assert data["username"] == payload["username"]
        assert data["email"] == payload["email"]
        assert "id" in data                                            # проверяем, что сервер вернул уникальный идентификатор созданного объекта