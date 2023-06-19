import requests

from credentials import ENDPOINT

SPOTIFY_TESTING_PLAYLIST_ID = "3cEYpjA9oz9GiPac4AsH4n"


def get_playlists_url(playlist_id, fields):
    return f"{ENDPOINT}/playlists/{playlist_id}?fields={fields}"


def test_get_playlist_expect_200_returned(access_token):
    existing_playlist_url = get_playlists_url(SPOTIFY_TESTING_PLAYLIST_ID, "")
    headers = {"Authorization": access_token}
    response = requests.get(existing_playlist_url, headers=headers)

    assert response.status_code == 200
