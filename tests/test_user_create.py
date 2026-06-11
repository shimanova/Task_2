import allure
import pytest
from api_client import create_user_api
from helpers import generate_new_user_data
from test_data import ErrorMessages


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        email, password, name = generate_new_user_data()
        response = create_user_api(email, password, name)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        assert response.json()["user"]["email"] == email
        assert response.json()["user"]["name"] == name

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        email, password, name = generate_new_user_data()
        create_user_api(email, password, name)
        response_duplicate = create_user_api(email, password, name)

        assert response_duplicate.status_code == 403
        assert response_duplicate.json()["message"] == ErrorMessages.USER_EXISTS

    @allure.title("Создание пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        email, password, name = generate_new_user_data()
        payload = {"email": email, "password": password, "name": name}
        del payload[missing_field]

        response = create_user_api(payload.get("email"), payload.get("password"), payload.get("name"))
        assert response.status_code == 403
        assert response.json()["message"] == ErrorMessages.MISSING_FIELDS