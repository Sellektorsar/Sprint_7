import requests
import allure
from data import COURIER_URL, COURIER_LOGIN_URL, ORDERS_URL
from utils import generate_random_string

@allure.step('Регистрация нового курьера')
def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(COURIER_URL, json=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    return login_pass

@allure.step('Удаление курьера')
def delete_courier(courier_id):
    response = requests.delete(COURIER_URL + f'/{courier_id}')
    return response

@allure.step('Создание заказа')
def create_order(color=None):
    from data import ORDER_DATA
    payload = ORDER_DATA.copy()
    payload['color'] = color or []
    response = requests.post(ORDERS_URL, json=payload)
    if response.status_code == 201:
        return response.json()['track']
    return None

@allure.step('Получение ID заказа по треку')
def get_order_id(track):
    response = requests.get(ORDERS_URL + '/track', params={'t': str(track)})
    if response.status_code == 200:
        return response.json()['order']['id']
    return None

@allure.step('Принятие заказа')
def accept_order(order_id, courier_id):
    response = requests.put(ORDERS_URL + f'/accept/{order_id}', params={'courierId': courier_id})
    return response