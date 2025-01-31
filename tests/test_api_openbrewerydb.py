import pytest
import requests


def test_api_breweries():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")
    assert response.status_code == 200
    assert "id" in response.text


def get_list_of_ids():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")
    result = response.json()
    ids = [item["id"] for item in result]
    return ids


@pytest.mark.parametrize("breweries_id", get_list_of_ids())
def test_api_breweries_by_id(breweries_id):
    response = requests.get(
        f"https://api.openbrewerydb.org/v1/breweries/{breweries_id}"
    )
    assert response.status_code == 200
    result = response.json()
    assert result["id"] == breweries_id


def get_list_of_cities():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries")
    result = response.json()
    cities = [item["city"] for item in result]
    return cities


@pytest.mark.parametrize("city", get_list_of_cities())
def test_api_breweries_by_city(city):
    response = requests.get(
        f"https://api.openbrewerydb.org/v1/breweries?by_city={city}"
    )
    assert response.status_code == 200
    result = response.json()
    assert all(item["city"] == city for item in result)


@pytest.mark.parametrize(
    "requested_number, expected_number",
    [(1, 1), (55, 55), (130, 130), (200, 200), (250, 200)],
)
def test_api_breweries_by_number_of_breweries_by_page(
    requested_number, expected_number
):
    response = requests.get(
        f"https://api.openbrewerydb.org/v1/breweries?per_page={requested_number}"
    )
    assert response.status_code == 200
    result = response.json()
    length = len(result)
    assert length == expected_number


def test_api_random_breweries():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
    result = response.json()
    assert response.status_code == 200
    assert "id" in response.text
    assert len(result) == 1
