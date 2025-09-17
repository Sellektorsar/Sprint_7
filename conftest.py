import pytest
import requests
from api import register_new_courier_and_return_login_password, delete_courier, create_order
from data import COURIER_LOGIN_URL

@pytest.fixture
def courier():
    """Фикстура для создания курьера и очистки после теста"""
    courier_data = register_new_courier_and_return_login_password()
    login, password, first_name = courier_data
    # Получить идентификатор курьера
    response = requests.post(COURIER_LOGIN_URL, json={"login": login, "password": password})
    courier_id = response.json()['id']
    yield login, password, courier_id
    # Очистка
    delete_courier(courier_id)

@pytest.fixture
def order():
    """Фикстура для создания заказа"""
    track = create_order()
    return track