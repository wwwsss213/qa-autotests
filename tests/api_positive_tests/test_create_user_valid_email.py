import pytest


@pytest.mark.api
@pytest.mark.parametrize(
    "email",
    [
        "test@example.com",
        "user123@gmail.com",
        "first.last@example.com"
    ]
)
def test_create_user_valid_email(
    api_client,
    base_url,
    user_data,
    email
):
    # ARRANGE
    user_data["email"] = email

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 201
