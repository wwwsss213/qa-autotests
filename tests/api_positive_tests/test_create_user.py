import pytest


@pytest.mark.api
def test_create_user(api_client, base_url, user_data): # Согласно требованиям API, допустимая длина name: 2–100 символов
    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert response.status_code == 201

    data = response.json()

    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]
    assert data["is_active"] is True
    assert "id" in data
    assert "created_at" in data


@pytest.mark.api
def test_get_user_by_id(api_client, base_url, user_data):
    # ARRANGE
    create_response = api_client.post(
        base_url,
        json=user_data
    )

    assert create_response.status_code == 201

    user_id = create_response.json()["id"]

    # ACT
    response = api_client.get(
        f"{base_url}/{user_id}"
    )

    # ASSERT
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]
    assert data["is_active"] is True