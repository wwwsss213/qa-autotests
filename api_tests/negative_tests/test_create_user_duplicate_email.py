@pytest.mark.api
def test_create_user_duplicate_email(api_client, base_url, user_data):
    # ACT
    first_response = api_client.post(
        base_url,
        json=user_data
    )

    second_response = api_client.post(
        base_url,
        json=user_data
    )

    # ASSERT
    assert first_response.status_code == 201
    assert second_response.status_code in [400, 409]