import requests

from credentials import ENDPOINT

SPOTIFY_TESTING_PLAYLIST_ID = "3cEYpjA9oz9GiPac4AsH4n"


def get_category_playlists_url(category_id, params, access_token):
    return requests.get(f"{ENDPOINT}/browse/categories/{category_id}/playlists", params, headers={"Authorization": access_token})


def test_get_playlist_expect_200_returned(access_token):
    response = get_category_playlists_url("dinner", {"limit": 50, "country": "PL"}, access_token)

    assert response.status_code == 200


def test_get_playlist_expect_k_pop_to_be_more_popular_then_dinner_category(access_token):
    k_pop_category = "0JQ5DAqbMKFGvOw3O4nLAf"
    response_k_pop = get_category_playlists_url(k_pop_category, {"limit": 50, "country": "PL"}, access_token)
    response_dinner = get_category_playlists_url("dinner", {"limit": 50, "country": "PL"}, access_token)

    body_k_pop = response_k_pop.json()
    body_dinner = response_dinner.json()

    assert len(body_k_pop["playlists"]["items"]) > len(body_dinner["playlists"]["items"])