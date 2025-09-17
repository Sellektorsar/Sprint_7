import requests
import allure
from api import delete_courier
from data import COURIER_URL, ERROR_COURIER_NOT_FOUND_SHORT

class TestDeleteCourier:

    @allure.title('Удалить курьера успешно')
    def test_delete_courier_success(self, courier):
        login, password, courier_id = courier
        delete_response = delete_courier(courier_id)
        assert delete_response.status_code == 200
        assert delete_response.json() == {"ok": True}

    @allure.title('Удалить курьера без id')
    def test_delete_courier_no_id(self):
        response = requests.delete(COURIER_URL + '/')
        assert response.status_code == 404
        # Разбор тела ответа
        data = response.json()
        assert 'message' in data

    @allure.title('Удалить курьера с неправильным id')
    def test_delete_courier_wrong_id(self):
        response = requests.delete(COURIER_URL + '/999999')
        assert response.status_code == 404
        data = response.json()
        # На этой ручке приходит короткая форма сообщения
        assert data['message'] == ERROR_COURIER_NOT_FOUND_SHORT