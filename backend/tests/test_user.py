import pytest
from fastapi.testclient import TestClient

def test_register_user(client: TestClient):
    url = "/users/register"
    payload = {
        "username": "adish",
        "email": "adish@gmail.com",
        "phone": "8606435818",
        "password": "password123"
    }

    response = client.post(url, json=payload)

    # Because you set status_code=201 in your router
    assert response.status_code == 201

    data = response.json()
    assert data["username"] == "adish"
    assert data["email"] == "adish@gmail.com"
    assert data["phone"] == "8606435818"
    assert "id" in data
