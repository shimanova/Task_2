import requests
import allure
from test_data import Urls


class UserApi:
    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return requests.post(Urls.CREATE_USER, json=payload)

    @staticmethod
    @allure.step("Отправка запроса на логин пользователя")
    def login_user(email, password):
        payload = {"email": email, "password": password}
        return requests.post(Urls.LOGIN_USER, json=payload)

    @staticmethod
    @allure.step("Отправка запроса на изменение данных пользователя")
    def change_user(access_token, email=None, password=None, name=None):
        payload = {}
        if email:
            payload["email"] = email
        if password:
            payload["password"] = password
        if name:
            payload["name"] = name
        headers = {"Authorization": access_token}
        return requests.patch(Urls.CHANGE_USER, json=payload, headers=headers)

    @staticmethod
    @allure.step("Отправка запроса на изменение данных пользователя без авторизации")
    def change_user_unauthorized(email=None, password=None, name=None):
        payload = {}
        if email:
            payload["email"] = email
        if password:
            payload["password"] = password
        if name:
            payload["name"] = name
        return requests.patch(Urls.CHANGE_USER, json=payload)

    @staticmethod
    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        return requests.delete(Urls.CHANGE_USER, headers=headers)


class OrderApi:
    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(ingredients, access_token=None):
        payload = {"ingredients": ingredients}
        headers = {"Authorization": access_token} if access_token else {}
        return requests.post(Urls.CREATE_ORDER, json=payload, headers=headers)

    @staticmethod
    @allure.step("Отправка запроса на получение заказов пользователя")
    def get_user_orders(access_token):
        headers = {"Authorization": access_token}
        return requests.get(Urls.GET_USER_ORDERS, headers=headers)

    @staticmethod
    @allure.step("Отправка запроса на получение заказов пользователя без авторизации")
    def get_user_orders_unauthorized():
        return requests.get(Urls.GET_USER_ORDERS)