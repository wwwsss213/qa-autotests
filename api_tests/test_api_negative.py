import requests


def test_create_user_duplicate_email(base_url, user_data):
    # ARRANGE
    session = requests.Session()
    session.trust_env = False

    # ACT
    first_response = session.post(base_url, json=user_data)
    second_response = session.post(base_url, json=user_data)

    # ASSERT
    assert first_response.status_code == 201
    assert second_response.status_code in [400, 409]


def test_create_user_invalid_email(base_url, user_data):
    # ARRANGE
    session = requests.Session()
    session.trust_env = False

    user_data["email"] = "invalid-email"

    # ACT
    response = session.post(base_url, json=user_data)

    # ASSERT
    assert response.status_code == 422


def test_create_user_invalid_age(base_url, user_data):
    # ARRANGE
    session = requests.Session()
    session.trust_env = False

    user_data["age"] = -1

    # ACT
    response = session.post(base_url, json=user_data)

    # ASSERT
    assert response.status_code == 422


def test_get_user_not_found(base_url):
    # ARRANGE
    session = requests.Session()
    session.trust_env = False

    # ACT
    response = session.get(f"{base_url}/999999")

    # ASSERT
    assert response.status_code == 404