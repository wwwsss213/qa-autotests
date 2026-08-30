import requests


def test_create_user(base_url, user_data):
    # ARRANGE
    session = requests.Session()
    session.trust_env = False

    # ACT
    response = session.post(
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