import pytest
import requests  # <-- добавили импорт
import allure
from api_client import create_user_api, login_user_api
from helpers import generate_new_user_data
from test_data import Urls


@pytest.fixture
def create_and_delete_user():
    email, password, name = generate_new_user_data()
    response_create = create_user_api(email, password, name)

    with allure.step("Создание нового пользователя через фикстуру"):
        access_token = None
        if response_create.status_code == 200:
            access_token = response_create.json().get("accessToken")

    yield email, password, name, access_token

    with allure.step("Удаление пользователя через фикстуру"):
        if access_token:
            # Не используем login_user_api, просто удаляем через API с токеном
            delete_response = requests.delete(Urls.CHANGE_USER, headers={"Authorization": access_token})