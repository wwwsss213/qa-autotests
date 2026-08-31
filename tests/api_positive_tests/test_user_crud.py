import pytest


@pytest.mark.e2e
def test_user_crud(api_client, base_url, user_data, db_cursor):
    # CREATE
    create_response = api_client.post(
        base_url,
        json=user_data
    )

    assert create_response.status_code == 201

    user_id = create_response.json()["id"]

    # READ
    get_response = api_client.get(
        f"{base_url}/{user_id}"
    )

    assert get_response.status_code == 200

    data = get_response.json()

    assert data["id"] == user_id
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]

    # UPDATE
    update_data = {
        "name": "Updated User",
        "email": user_data["email"],
        "age": 30,
        "is_active": True
    }

    update_response = api_client.patch(
        f"{base_url}/{user_id}",
        json=update_data
    )

    assert update_response.status_code == 200

    data = update_response.json()

    assert data["name"] == update_data["name"]
    assert data["age"] == update_data["age"]

    # DELETE
    delete_response = api_client.delete(
        f"{base_url}/{user_id}"
    )

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "User deleted"
    assert delete_response.json()["id"] == user_id

    # VERIFY DB
    db_cursor.execute(
        "SELECT COUNT(*) FROM users WHERE id = %s;",
        (user_id,)
    )

    user_count = db_cursor.fetchone()[0]

    assert user_count == 0