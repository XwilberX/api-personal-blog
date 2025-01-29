import niquests
from pprint import pp

from config.config import get_settings

settings = get_settings(env_file=".env.test")


def test_example():
    assert True


def test_auth_login(base_url):
    body = {
        "email": "wilber.alegria99@gmail.com",
        "password": "@Mendez99",
    }

    response = niquests.post(f"{base_url}{settings.api_prefix}/auth/login", json=body)

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    assert response.json()["data"]["user"]["email"] == body["email"]


def test_auth_register(base_url):
    body = {
        "first_name": "Wilber",
        "middle_name": "Alexander",
        "last_name": "Alegria",
        "username": "wilberalegria",
        "email": "wilberalegria@mail.com",
        "password": "123456",
    }

    response = niquests.post(
        f"{base_url}{settings.api_prefix}/auth/register", json=body
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "Success"
