import requests

from credentials import ENDPOINT


def change_playlists_url(playlist_id):
    return f"{ENDPOINT}/playlists/{playlist_id}"


def test_change_playlist_name_expect_200_returned(access_token, new_playlist_id):
    changed_playlist_url = change_playlists_url(new_playlist_id)
    headers = {"Authorization": access_token}

    body = {"name": "New Title", "description": "Sample playlist for testing", "public": False}
    response = requests.put(changed_playlist_url, data=None, json=body, headers=headers)

    assert response.status_code == 200


def test_empty_playlist_name_expect_400_returned(access_token, new_playlist_id):
    changed_playlist_url = change_playlists_url(new_playlist_id)
    headers = {"Authorization": access_token}

    body = {"name": " ", "description": "Sample playlist for testing", "public": False}
    response = requests.put(changed_playlist_url, data=None, json=body, headers=headers)

    assert response.status_code == 400