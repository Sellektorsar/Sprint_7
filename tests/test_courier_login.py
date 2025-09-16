import requests
import allure
from data import COURIER_LOGIN_URL, ERROR_LOGIN_FAILED, ERROR_MISSING_LOGIN_DATA
from utils import generate_random_string

class TestCourierLogin:

    @allure.title('Авторизация курьера успешно')
    def test_login_success(self, courier):
        login, password, courier_id = courier
        # Авторизация
        login_payload = {"login": login, "password": password}
        response = requests.post(COURIER_LOGIN_URL, json=login_payload)
        assert response.status_code == 200
        data = response.json()
        assert 'id' in data

    @allure.title('Авторизация с неправильным логином')
    def test_login_wrong_login(self):
        login_payload = {"login": "wronglogin", "password": "password"}
        response = requests.post(COURIER_LOGIN_URL, json=login_payload)
        assert response.status_code == 404
        data = response.json()
        assert data['message'] == ERROR_LOGIN_FAILED

    @allure.title('Авторизация с неправильным паролем')
    def test_login_wrong_password(self, courier):
        login, password, courier_id = courier
        # Авторизация с неправильным паролем
        login_payload = {"login": login, "password": "wrongpass"}
        response = requests.post(COURIER_LOGIN_URL, json=login_payload)
        assert response.status_code == 404
        data = response.json()
        assert data['message'] == ERROR_LOGIN_FAILED

    @allure.title('Авторизация без поля login')
    def test_login_missing_login(self):
        login_payload = {"password": "password"}
        response = requests.post(COURIER_LOGIN_URL, json=login_payload)
        assert response.status_code == 400
        data = response.json()
        assert data['message'] == ERROR_MISSING_LOGIN_DATA

    @allure.title('Авторизация без поля password')
    def test_login_missing_password(self):
        login_payload = {"login": "login"}
        response = requests.post(COURIER_LOGIN_URL, json=login_payload)
        assert response.status_code == 504  # API возвращает 504 при отсутствии пароля

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_non_existent(self):
        login_payload = {"login": generate_random_string(10), "password": generate_random_string(10)}
        response = requests.post(COURIER_LOGIN_URL, json=login_payload)
        assert response.status_code == 404
        data = response.json()
        assert data['message'] == ERROR_LOGIN_FAILED