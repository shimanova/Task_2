import pytest
from api_client import UserApi
from helpers import generate_new_user_data


@pytest.fixture
def create_and_delete_user():
    email, password, name = generate_new_user_data()
    response = UserApi.create_user(email, password, name)
    access_token = response.json().get("accessToken") if response.status_code == 200 else None

    yield email, password, name, access_token

    if access_token:
        UserApi.delete_user(access_token)