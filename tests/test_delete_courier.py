import requests
import allure
from tests.helpers import generate_random_string, register_new_courier_and_return_login_password, delete_courier

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

class TestDeleteCourier:

    @allure.step('Удалить курьера успешно')
    def test_delete_courier_success(self, courier):
        login, password, courier_id = courier
        # Удалить
        delete_response = delete_courier(courier_id)
        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    @allure.step('Удалить курьера без id')
    def test_delete_courier_no_id(self):
        # Попытаться удалить без id, возможно 404
        response = requests.delete(BASE_URL + 'courier/')
        assert response.status_code == 404

    @allure.step('Удалить курьера с неправильным id')
    def test_delete_courier_wrong_id(self):
        response = requests.delete(BASE_URL + 'courier/999999')
        assert response.status_code == 404