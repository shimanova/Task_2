import allure
import requests
from test_data import Urls


@allure.step("Отправка запроса на создание пользователя")
def create_user_api(email, password, name):
    payload = {"email": email, "password": password, "name": name}
    return requests.post(Urls.CREATE_USER, json=payload)


@allure.step("Отправка запроса на логин пользователя")
def login_user_api(email, password):
    payload = {"email": email, "password": password}
    return requests.post(Urls.LOGIN_USER, json=payload)


@allure.step("Отправка запроса на изменение данных пользователя")
def change_user_api(access_token, email=None, password=None, name=None):
    payload = {}
    if email:
        payload["email"] = email
    if password:
        payload["password"] = password
    if name:
        payload["name"] = name
    headers = {"Authorization": access_token}
    return requests.patch(Urls.CHANGE_USER, json=payload, headers=headers)


@allure.step("Отправка запроса на изменение данных пользователя без авторизации")
def change_user_unauthorized_api(email=None, password=None, name=None):
    payload = {}
    if email:
        payload["email"] = email
    if password:
        payload["password"] = password
    if name:
        payload["name"] = name
    return requests.patch(Urls.CHANGE_USER, json=payload)


@allure.step("Отправка запроса на создание заказа")
def create_order_api(ingredients, access_token=None):
    payload = {"ingredients": ingredients}
    headers = {}
    if access_token:
        headers["Authorization"] = access_token
    return requests.post(Urls.CREATE_ORDER, json=payload, headers=headers)


@allure.step("Отправка запроса на получение заказов пользователя")
def get_user_orders_api(access_token):
    headers = {"Authorization": access_token}
    return requests.get(Urls.GET_USER_ORDERS, headers=headers)


@allure.step("Отправка запроса на получение заказов пользователя без авторизации")
def get_user_orders_unauthorized_api():
    return requests.get(Urls.GET_USER_ORDERS)