def test_user_login(client):
    url = "/users/login"

    pay_load = {
        "username": "adish",
        "password": "password123"
    }

    response = client.post(url, json=pay_load)

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_user_login_with_invalid_credentials(client):
    url = "/users/login"

    pay_load = {
        "username": "adish",
        "password" : "password"
    }

    response = client.post(url, json=pay_load)

    assert response.status_code == 400
    data = response.json()
    assert "Invalid" in data["detail"]