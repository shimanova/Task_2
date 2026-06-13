import allure
import pytest
from api_client import UserApi
from helpers import generate_new_user_data
from test_data import ErrorMessages


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_and_delete_user):
        email, password, name, access_token = create_and_delete_user
        response = UserApi.login_user(email, password)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == email
        assert response.json()["user"]["name"] == name

    @allure.title("Логин с неверными учётными данными")
    @pytest.mark.parametrize("wrong_email, wrong_password", [
        ("wrong@test.ru", "correct"),
        ("correct@test.ru", "wrong"),
        ("wrong@test.ru", "wrong"),
    ])
    def test_login_invalid_credentials(self, create_and_delete_user, wrong_email, wrong_password):
        email, password, name, access_token = create_and_delete_user
        login_email = wrong_email if "wrong" in wrong_email else email
        login_password = wrong_password if "wrong" in wrong_password else password

        response = UserApi.login_user(login_email, login_password)
        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessages.LOGIN_INCORRECT