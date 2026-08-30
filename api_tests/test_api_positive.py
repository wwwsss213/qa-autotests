import pytest


@pytest.mark.api
def test_create_user(api_client, base_url, user_data):
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

