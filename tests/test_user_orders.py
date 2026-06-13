import allure
from api_client import OrderApi
from test_data import ErrorMessages


@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, create_and_delete_user):
        _, _, _, access_token = create_and_delete_user
        response = OrderApi.get_user_orders(access_token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_without_auth(self):
        response = OrderApi.get_user_orders_unauthorized()

        assert response.status_code == 401
        assert response.json()["message"] == ErrorMessages.UNAUTHORIZED