import pytest


@pytest.mark.e2e
def test_create_user_and_verify_in_db(api_client, base_url, user_data, db_cursor):
    # ARRANGE
    target_email = user_data["email"]

    # ACT
    response = api_client.post(
        base_url,
        json=user_data
    )

    db_cursor.execute(
        "SELECT name, email, age, is_active "
        "FROM users WHERE email = %s;",
        (target_email,)
    )
    db_result = db_cursor.fetchone()

    # ASSERT — API
    assert response.status_code == 201

    data = response.json()

    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert data["age"] == user_data["age"]
    assert data["is_active"] is True

    # ASSERT — DB
    assert db_result is not None
    assert db_result[0] == user_data["name"]
    assert db_result[1] == user_data["email"]
    assert db_result[2] == user_data["age"]
    assert db_result[3] is True


@pytest.mark.e2e
def test_duplicate_email_not_created_in_db(
        api_client,
        base_url,
        user_data,
        db_cursor
):
    # ARRANGE
    target_email = user_data["email"]

    # ACT
    first_response = api_client.post(
        base_url,
        json=user_data
    )

    second_response = api_client.post(
        base_url,
        json=user_data
    )

    db_cursor.execute(
        "SELECT COUNT(*) FROM users WHERE email = %s;",
        (target_email,)
    )
    email_count = db_cursor.fetchone()[0]

    # ASSERT
    assert first_response.status_code == 201
    assert second_response.status_code in [400, 409]
    assert email_count == 1