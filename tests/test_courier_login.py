import pytest
import requests
import allure
from tests.helpers import generate_random_string

class TestCourierLogin:

    @allure.step('Авторизация курьера успешно')
    def test_login_success(self, courier):
        login, password, courier_id = courier
        # Авторизация
        login_payload = {"login": login, "password": password}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.step('Авторизация с неправильным логином')
    def test_login_wrong_login(self):
        login_payload = {"login": "wronglogin", "password": "password"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.step('Авторизация с неправильным паролем')
    def test_login_wrong_password(self, courier):
        login, password, courier_id = courier
        # Авторизация с неправильным паролем
        login_payload = {"login": login, "password": "wrongpass"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.step('Авторизация без поля login')
    def test_login_missing_login(self):
        login_payload = {"password": "password"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_payload)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message", "")

    @allure.step('Авторизация без поля password')
    def test_login_missing_password(self):
        login_payload = {"login": "login"}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_payload)
        assert response.status_code == 504  # API возвращает 504 при отсутствии пароля

    @allure.step('Авторизация несуществующего пользователя')
    def test_login_non_existent(self):
        from helpers import generate_random_string
        login_payload = {"login": generate_random_string(10), "password": generate_random_string(10)}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', json=login_payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")