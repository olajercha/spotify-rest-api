import requests

from credentials import ENDPOINT


def add_items_url(playlist_id):
    return f"{ENDPOINT}/playlists/{playlist_id}/tracks"


def remove_items_url(playlist_id):
    return f"{ENDPOINT}/playlists/{playlist_id}/tracks"


def test_add_items_to_playlist_expect_201_returned(access_token, new_playlist_id):
    existing_playlist_url = add_items_url(new_playlist_id)
    headers = {"Authorization": access_token, "Content-Type": "application/json"}
    body = {"uris": ["spotify:track:0HqZX76SFLDz2aW8aiqi7G"]}
    response = requests.post(existing_playlist_url, headers=headers, json=body)

    assert response.status_code == 201


def test_remove_playlist_items_expect_200_returned(access_token, new_playlist_id):
    existing_playlist_url = remove_items_url(new_playlist_id)
    headers = {"Authorization": access_token}
    body = {"tracks": [{"uri": "spotify:track:0HqZX76SFLDz2aW8aiqi7G", "positions": [0]}]}
    response = requests.delete(existing_playlist_url, headers=headers, json=body)

    assert response.status_code == 200