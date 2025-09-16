import requests
import allure
from api import get_order_id, accept_order
from data import ORDERS_URL

class TestAcceptOrder:

    @allure.title('Принять заказ успешно')
    def test_accept_order_success(self, courier, order):
        login, password, courier_id = courier
        track = order
        order_id = get_order_id(track)
        assert order_id is not None
        # Принять заказ
        accept_response = accept_order(order_id, courier_id)
        assert accept_response.status_code == 200
        data = accept_response.json()
        assert data == {"ok": True}

    @allure.title('Принять заказ без id курьера')
    def test_accept_order_no_courier(self, order):
        track = order
        order_id = get_order_id(track)
        assert order_id is not None
        # Принять без courierId
        response = requests.put(ORDERS_URL + '/accept/' + str(order_id))
        assert response.status_code == 400
        data = response.json()
        # Assuming error message, but since not specified, just status

    @allure.title('Принять заказ с неправильным id курьера')
    def test_accept_order_wrong_courier(self, order):
        track = order
        order_id = get_order_id(track)
        assert order_id is not None
        # Принять с неправильным courierId
        response = requests.put(ORDERS_URL + '/accept/' + str(order_id), params={'courierId': 999999})
        assert response.status_code == 404
        data = response.json()
        # Assuming error message

    @allure.title('Принять заказ без id заказа')
    def test_accept_order_no_order(self, courier):
        login, password, courier_id = courier
        # Принять без id заказа
        response = requests.put(ORDERS_URL + '/accept/', params={'courierId': courier_id})
        assert response.status_code == 404
        data = response.json()
        # Assuming error message

    @allure.title('Принять заказ с неправильным id заказа')
    def test_accept_order_wrong_order(self, courier):
        login, password, courier_id = courier
        # Принять с неправильным id заказа
        response = requests.put(ORDERS_URL + '/accept/999999', params={'courierId': courier_id})
        assert response.status_code == 404
        data = response.json()
        # Assuming error message