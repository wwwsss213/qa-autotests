import pytest


@pytest.mark.api
def test_create_user_duplicate_email(api_client, base_url, user_data):
    # ACT
    first_response = api_client.post(
        base_url,
        json=user_data
    )

    second_response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert first_response.status_code == 201
    assert second_response.status_code in [400, 409]


@pytest.mark.api
def test_create_user_invalid_email(api_client, base_url, user_data):
    # ARRANGE
    user_data["email"] = "invalid-email"

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 422


@pytest.mark.api
def test_create_user_invalid_age(api_client, base_url, user_data):
    # ARRANGE
    user_data["age"] = -1

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 422


@pytest.mark.api
def test_get_user_not_found(api_client, base_url):
    # ACT
    response = api_client.get(
        f"{base_url}/999999"
    )

    # ASSERT
    assert response.status_code == 404