import allure
import pytest
from api_client import OrderApi
from test_data import TestData, ErrorMessages


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self, create_and_delete_user):
        _, _, _, access_token = create_and_delete_user
        response = OrderApi.create_order(TestData.VALID_INGREDIENTS, access_token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации, но с ингредиентами")
    def test_create_order_without_auth(self):
        response = OrderApi.create_order(TestData.VALID_INGREDIENTS)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, create_and_delete_user):
        _, _, _, access_token = create_and_delete_user
        response = OrderApi.create_order([], access_token)

        assert response.status_code == 400
        assert response.json()["message"] == ErrorMessages.NO_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, create_and_delete_user):
        _, _, _, access_token = create_and_delete_user
        response = OrderApi.create_order([TestData.INVALID_HASH], access_token)

        assert response.status_code == 500