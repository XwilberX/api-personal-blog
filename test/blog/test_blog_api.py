import niquests
from pprint import pp

from config.config import get_settings

settings = get_settings(env_file=".env.test")


def test_example():
    assert True


def test_blog_get_all(base_url, api_token):
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/blogs/",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) > 0


def test_blog_get_all_with_author(base_url, api_token):
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/blogs/all",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) > 0


def test_blog_get_by_pk(base_url, api_token):
    # obtener un blog de la lista
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/blogs/",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    if not response.json()["status_code"] == 200:
        assert False

    pk = response.json()["data"][0]["pk"]

    # obtener el blog por pk
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/blogs/find/{pk}",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"]["pk"] == pk


def test_blog_create(base_url, api_token):
    # obtener un usuario
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/users",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    pp(response.json())

    if not response.json()["status_code"] == 200:
        assert False

    user_pk = response.json()["data"][0]["pk"]

    body = {
        "title": "Test blog",
        "description": "This is a test blog",
        "content": "This is a test blog",
        "author": {"pk": user_pk},
    }

    response = niquests.post(
        f"{base_url}{settings.api_prefix}/blogs/create",
        headers={"Authorization": f"Bearer {api_token}"},
        json=body,
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"]["title"] == body["title"]


def test_blog_update(base_url, api_token):
    # obtener un blog
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/blogs/",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    pp(response.json())

    if not response.json()["status_code"] == 200:
        assert False

    pk = response.json()["data"][0]["pk"]

    body = {
        "title": "Test blog updated",
        "description": "This is a test blog updated",
        "content": "This is a test blog updated",
    }

    response = niquests.put(
        f"{base_url}{settings.api_prefix}/blogs/update/{pk}",
        headers={"Authorization": f"Bearer {api_token}"},
        json=body,
    )

    pp(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"]["title"] == body["title"]


def test_blog_delete(base_url, api_token):
    # obtener un blog
    response = niquests.get(
        f"{base_url}{settings.api_prefix}/blogs/",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    pp(response.json())

    if not response.json()["status_code"] == 200:
        assert False

    pk = response.json()["data"][0]["pk"]

    response = niquests.delete(
        f"{base_url}{settings.api_prefix}/blogs/delete/{pk}",
        headers={"Authorization": f"Bearer {api_token}"},
    )

    assert response.status_code == 200
