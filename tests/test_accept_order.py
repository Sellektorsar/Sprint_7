import requests
import allure
from api import get_order_id, accept_order
from data import ORDERS_URL, ERROR_MISSING_COURIER_ID, ERROR_COURIER_NOT_FOUND, ERROR_ORDER_NOT_FOUND

class TestAcceptOrder:

    @allure.title('Принять заказ успешно')
    def test_accept_order_success(self, courier, order):
        login, password, courier_id = courier
        track = order
        order_id = get_order_id(track)
        # Принять заказ
        accept_response = accept_order(order_id, courier_id)
        assert accept_response.status_code == 200
        data = accept_response.json()
        assert data == {"ok": True}

    @allure.title('Принять заказ без id курьера')
    def test_accept_order_no_courier(self, order):
        track = order
        order_id = get_order_id(track)
        # Принять заказ без параметра идентификатора курьера
        response = requests.put(ORDERS_URL + '/accept/' + str(order_id))
        assert response.status_code == 400
        data = response.json()
        assert data['message'] == ERROR_MISSING_COURIER_ID

    @allure.title('Принять заказ с неправильным id курьера')
    def test_accept_order_wrong_courier(self, order):
        track = order
        order_id = get_order_id(track)
        # Принять заказ с неверным идентификатором курьера
        response = requests.put(ORDERS_URL + '/accept/' + str(order_id), params={'courierId': 999999})
        assert response.status_code == 404
        data = response.json()
        assert data['message'] == ERROR_COURIER_NOT_FOUND

    @allure.title('Принять заказ без id заказа')
    def test_accept_order_no_order(self, courier):
        login, password, courier_id = courier
        # Принять без идентификатора заказа
        response = requests.put(ORDERS_URL + '/accept/', params={'courierId': courier_id})
        assert response.status_code == 404
        # Разбор тела ответа
        try:
            data = response.json()
            assert 'message' in data
        except ValueError:
            # Ответ не в формате JSON — как минимум должен быть непустой текст
            assert response.text is not None and response.text != ''

    @allure.title('Принять заказ с неправильным id заказа')
    def test_accept_order_wrong_order(self, courier):
        login, password, courier_id = courier
        # Принять с неверным идентификатором заказа
        response = requests.put(ORDERS_URL + '/accept/999999', params={'courierId': courier_id})
        assert response.status_code == 404
        data = response.json()
        assert data['message'] == ERROR_ORDER_NOT_FOUND