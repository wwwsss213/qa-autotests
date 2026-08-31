import pytest


@pytest.mark.api
@pytest.mark.parametrize("name", ["A", "A" * 101, ""])
def test_create_user_invalid_name(
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
    assert response.status_code == 422