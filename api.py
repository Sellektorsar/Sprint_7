import requests
import allure
from data import COURIER_URL, COURIER_LOGIN_URL, ORDERS_URL, ORDER_DATA
from utils import generate_random_string


class CourierApi:
    """Клиент для работы с ручками курьеров"""

    @allure.step('Регистрация нового курьера')
    def register(self, login: str, password: str, first_name: str):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(COURIER_URL, json=payload)

    @allure.step('Логин курьера')
    def login(self, login: str, password: str):
        payload = {"login": login, "password": password}
        return requests.post(COURIER_LOGIN_URL, json=payload)

    @allure.step('Удаление курьера')
    def delete(self, courier_id: int):
        return requests.delete(f"{COURIER_URL}/{courier_id}")


class OrdersApi:
    """Клиент для работы с ручками заказов"""

    @allure.step('Создание заказа')
    def create(self, color=None):
        payload = ORDER_DATA.copy()
        payload['color'] = color or []
        return requests.post(ORDERS_URL, json=payload)

    @allure.step('Получение заказа по треку')
    def get_by_track(self, track: str):
        return requests.get(f"{ORDERS_URL}/track", params={'t': str(track)})

    @allure.step('Принятие заказа')
    def accept(self, order_id: int, courier_id: int):
        return requests.put(f"{ORDERS_URL}/accept/{order_id}", params={'courierId': courier_id})


# Процедурные обёртки (для совместимости с существующими тестами)

@allure.step('Регистрация нового курьера')
def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    response = CourierApi().register(login, password, first_name)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass


@allure.step('Удаление курьера')
def delete_courier(courier_id):
    return CourierApi().delete(courier_id)


@allure.step('Создание заказа')
def create_order(color=None):
    response = OrdersApi().create(color)
    if response.status_code == 201:
        return response.json().get('track')
    return None


@allure.step('Получение ID заказа по треку')
def get_order_id(track):
    response = OrdersApi().get_by_track(track)
    if response.status_code == 200:
        return response.json().get('order', {}).get('id')
    return None


@allure.step('Принятие заказа')
def accept_order(order_id, courier_id):
    return OrdersApi().accept(order_id, courier_id)