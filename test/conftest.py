import pytest
import niquests

from config.config import get_settings

settings = get_settings(env_file=".env.test")

BASE_URL = "http://localhost:8080"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def api_token():
    body = {
        "email": "wilber.alegria99@gmail.com",
        "password": "@Mendez99",
    }

    response = niquests.post(f"{BASE_URL}{settings.api_prefix}/auth/login", json=body)

    return response.json()["data"]["token"]
