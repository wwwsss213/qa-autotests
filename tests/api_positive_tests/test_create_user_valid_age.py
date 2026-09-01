import pytest

@pytest.mark.api
# Согласно требованиям API, допустимый возраст: 0–130, также допускается null
@pytest.mark.parametrize("age", [0, 1, 65, 129, 130, None])
def test_create_user_valid_age(
    api_client,
    base_url,
    user_data,
    age
):
    # ARRANGE
    user_data["age"] = age

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 201
