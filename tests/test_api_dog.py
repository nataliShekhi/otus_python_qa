import pytest
import requests


def test_api_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200
    assert "message" in response.text
    assert "success" in response.text
    assert ".jpg" in response.text


@pytest.mark.parametrize(
    "requested_number, expected_number", [(1, 1), (25, 25), (50, 50), (101, 50)]
)
def test_api_dog_number_of_images(requested_number, expected_number):
    response = requests.get(
        f"https://dog.ceo/api/breeds/image/random/{requested_number}"
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["message"]) == expected_number


@pytest.mark.parametrize("number", [1, 25, 50, 101])
def test_api_dog_by_breed_number_of_images(number):
    response = requests.get(f"https://dog.ceo/api/breed/hound/images/random/{number}")
    assert response.status_code == 200
    data = response.json()
    length = len(data["message"])
    assert number == length


def test_api_dog_by_sub_breed_and_get_sub_breeds():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    assert response.status_code == 200
    assert "message" in response.text
    assert "success" in response.text


def get_list_of_sub_breed():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    result = response.json()
    list_of_sub_breed = result["message"]
    return list_of_sub_breed


@pytest.mark.parametrize("sub_breed", get_list_of_sub_breed())
def test_api_dog_by_sub_breed_random_image(sub_breed):
    response = requests.get(f"https://dog.ceo/api/breed/hound/{sub_breed}/images")
    result = response.json()
    assert response.status_code == 200
    assert all(sub_breed in url for url in result["message"])
