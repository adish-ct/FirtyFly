from http.client import responses



def test_register_user_duplicate_email(client):
    url = "/users/register"

    payload = {
        "username": "abhinand",
        "email": "abhinand@gmail.com",
        "phone": "1234569870",
        "password": "abhi123"
    }

    payload_with_duplicate_email = {
        "username": "meera",
        "email": "abhinand@gmail.com",
        "phone": "9876543210",
        "password": "meeraPass@123"
    }

    # First registration should pass
    response_1 = client.post(url, json=payload)
    assert response_1.status_code == 201

    # second registration should fail
    response_2 = client.post(url, json=payload_with_duplicate_email)
    assert response_2.status_code == 400 or response_2.status_code == 409
    assert "email" in response_2.json()["detail"].lower()


def test_register_user_duplicate_phone(client):
    url = "/users/register"

    payload = {
        "username": "abhi",
        "email": "abhi@gmail.com",
        "phone": "9874563210",
        "password": "abhi123"
    }

    payload_with_duplicate_phone = {
        "username": "arjun",
        "email": "arjun123@example.com",
        "phone": "9874563210",
        "password": "abhi123"
    }

    response_1 = client.post(url, json=payload)
    assert response_1.status_code == 201

    response_2 = client.post(url, json=payload_with_duplicate_phone)
    assert response_2.status_code == 409
    assert "phone" in response_2.json()["detail"].lower()


def test_register_user_duplicate_username(client):
    url = "/users/register"

    payload = {
        "username": "raja",
        "email": "raja@gmail.com",
        "phone": "9874321650",
        "password": "raja123"
    }

    payload_with_duplicate_username = {
        "username": "raja",
        "email": "neha.k@example.com",
        "phone": "000000000",
        "password": "nehaStrongPwd789"
    }

    response_1 = client.post(url, json=payload)
    assert response_1.status_code == 201

    response_2 = client.post(url, json=payload_with_duplicate_username)
    assert response_2.status_code == 409
    assert "username" in response_2.json()["detail"].lower()



