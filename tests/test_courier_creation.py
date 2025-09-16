import requests
import allure
from data import COURIER_URL, ERROR_MISSING_DATA, ERROR_DUPLICATE_LOGIN
from utils import generate_random_string
from api import delete_courier

class TestCourierCreation:

    @allure.title('Создать курьера успешно')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data == {"ok": True}
        # Очистка
        login_payload = {"login": login, "password": password}
        login_response = requests.post(COURIER_URL + '/login', json=login_payload)
        courier_id = login_response.json()['id']
        delete_courier(courier_id)

    @allure.title('Нельзя создать дубликат курьера')
    def test_create_courier_duplicate(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # Создать первого
        requests.post(COURIER_URL, json=payload)
        # Попытаться создать дубликат
        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 409
        data = response.json()
        assert data['message'] == ERROR_DUPLICATE_LOGIN
        # Очистка
        login_payload = {"login": login, "password": password}
        login_response = requests.post(COURIER_URL + '/login', json=login_payload)
        courier_id = login_response.json()['id']
        delete_courier(courier_id)

    @allure.title('Отсутствует поле login')
    def test_create_courier_missing_login(self):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 400
        data = response.json()
        assert data['message'] == ERROR_MISSING_DATA

    @allure.title('Отсутствует поле password')
    def test_create_courier_missing_password(self):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(COURIER_URL, json=payload)
        assert response.status_code == 400
        data = response.json()
        assert data['message'] == ERROR_MISSING_DATA

