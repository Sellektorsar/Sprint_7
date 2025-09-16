import pytest
import requests
import allure
from tests.helpers import generate_random_string, delete_courier

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

class TestCourierCreation:

    @allure.step('Создать курьера успешно')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(BASE_URL + 'courier', json=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        # Очистка
        login_payload = {"login": login, "password": password}
        login_response = requests.post(BASE_URL + 'courier/login', json=login_payload)
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            delete_courier(courier_id)

    @allure.step('Нельзя создать дубликат курьера')
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
        requests.post(BASE_URL + 'courier', json=payload)
        # Получить id для очистки
        login_payload = {"login": login, "password": password}
        login_response = requests.post(BASE_URL + 'courier/login', json=login_payload)
        courier_id = None
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
        # Попытаться создать дубликат
        response = requests.post(BASE_URL + 'courier', json=payload)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json().get("message", "")
        # Очистка
        if courier_id:
            delete_courier(courier_id)

    @allure.step('Отсутствует поле login')
    def test_create_courier_missing_login(self):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(BASE_URL + 'courier', json=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json().get("message", "")

    @allure.step('Отсутствует поле password')
    def test_create_courier_missing_password(self):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(BASE_URL + 'courier', json=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json().get("message", "")
