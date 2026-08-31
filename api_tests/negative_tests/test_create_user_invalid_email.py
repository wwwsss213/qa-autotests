import pytest


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
def test_create_user_without_email(api_client, base_url, user_data):
    # ARRANGE
    user_data.pop("email")

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 422