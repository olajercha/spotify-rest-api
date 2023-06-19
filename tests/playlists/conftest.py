import pytest
import requests

from credentials import ENDPOINT, USER_ID, ACCESS_TOKEN


def create_playlists_url(user_id):
    return f"{ENDPOINT}/users/{user_id}/playlists"


@pytest.fixture(scope="session")
def access_token():
    return f"Bearer {ACCESS_TOKEN}"


@pytest.fixture(scope="session", name="new_playlist_id")
def test_create_playlist_expect_201_returned(access_token):
    new_playlist_url = create_playlists_url(USER_ID)
    headers = {"Authorization": access_token}

    body = {"name": "Testing Playlist1", "description": "Sample playlist for testing", "public": False}
    response = requests.post(new_playlist_url, data=None, json=body, headers=headers)

    assert response.status_code == 201

    new_playlist_id = response.json()["id"]

    yield new_playlist_id