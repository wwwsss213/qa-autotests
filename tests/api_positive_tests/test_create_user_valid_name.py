import pytest


@pytest.mark.api
@pytest.mark.parametrize("name", ["AB", "ABC", "A" * 50, "A" * 99, "A" * 100])
def test_create_user_valid_name(
    api_client,
    base_url,
    user_data,
    name
):
    # ARRANGE
    user_data["name"] = name

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 201