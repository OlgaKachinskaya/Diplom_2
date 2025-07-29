import pytest
import requests
from data import BASE_URL, ENDPOINTS, TestData

@pytest.fixture
def registered_user():
    user = TestData.create_user()
    response = requests.post(ENDPOINTS["register"], json=user)
    assert response.status_code == 200
    user["access_token"] = response.json()["accessToken"]
    return user

@pytest.fixture
def auth_token(registered_user):
    return registered_user["access_token"]

@pytest.fixture
def ingredients():
    return TestData.get_ingredients()