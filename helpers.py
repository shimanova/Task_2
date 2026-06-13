import random
import string
import allure


@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.step("Генерация данных для нового пользователя")
def generate_new_user_data():
    email = f"{generate_random_string(8)}@test.ru"
    password = generate_random_string(8)
    name = generate_random_string(8)
    return email, password, name