import allure
import pytest
from api_client import UserApi
from helpers import generate_new_user_data
from test_data import ErrorMessages


@allure.feature("Изменение данных пользователя")
class TestChangeUser:

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_user_with_auth(self, create_and_delete_user):
        email, password, name, access_token = create_and_delete_user
        new_email, new_password, new_name = generate_new_user_data()

        response = UserApi.change_user(access_token, email=new_email, password=new_password, name=new_name)

        assert response.status_code == 200
        assert response.json()["user"]["email"] == new_email
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение данных пользователя без авторизации")
    def test_change_user_without_auth(self, create_and_delete_user):
        email, password, name, _ = create_and_delete_user
        new_email, new_password, new_name = generate_new_user_data()

        response = UserApi.change_user_unauthorized(email=new_email, password=new_password, name=new_name)

        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessages.UNAUTHORIZED