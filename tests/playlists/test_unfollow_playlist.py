import requests

from credentials import ENDPOINT


def unfollow_playlist_url(playlist_id):
    return f"{ENDPOINT}/playlists/{playlist_id}/followers"


def test_unfollow_playlist_expect_200_returned(access_token, new_playlist_id):
    new_playlist_url = unfollow_playlist_url(new_playlist_id)
    headers = {"Authorization": access_token}

    response = requests.delete(new_playlist_url, headers=headers)

    assert response.status_code == 200