import niquests
from pprint import pp
from faker import Faker

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
        "first_name": Faker().first_name(),
        "middle_name": Faker().last_name(),
        "last_name": Faker().last_name(),
        "username": Faker().user_name(),
        "email": Faker().email(),
        "password": Faker().password(),
    }

    response = niquests.post(
        f"{base_url}{settings.api_prefix}/auth/register", json=body
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "Success"
