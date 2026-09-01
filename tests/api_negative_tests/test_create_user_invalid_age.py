import pytest


@pytest.mark.api
@pytest.mark.parametrize("age", [-1, 131, 15.111, 150])
def test_create_user_invalid_age(
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
    assert response.status_code == 422


@pytest.mark.api
@pytest.mark.parametrize("age", [ "abc", "28.1",[], {}])
def test_create_user_invalid_age_type(
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
    assert response.status_code == 422