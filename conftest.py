import pytest
import requests
from tests.helpers import BASE_URL, register_new_courier_and_return_login_password, delete_courier, create_order

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def courier():
    """Фикстура для создания курьера и очистки после теста"""
    courier_data = register_new_courier_and_return_login_password()
    if not courier_data:
        pytest.skip("Не удалось создать курьера")
    login, password, first_name = courier_data
    # Получить id
    response = requests.post(BASE_URL + 'courier/login', json={"login": login, "password": password})
    assert response.status_code == 200
    courier_id = response.json()['id']
    yield login, password, courier_id
    # Очистка
    delete_courier(courier_id)

@pytest.fixture
def order():
    """Фикстура для создания заказа"""
    track = create_order()
    if not track:
        pytest.skip("Не удалось создать заказ")
    yield track
    # Очистка для заказов не реализована