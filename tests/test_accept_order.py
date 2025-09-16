import pytest
import requests
import allure
from tests.helpers import get_order_id, accept_order

class TestAcceptOrder:

    @allure.step('Принять заказ успешно')
    def test_accept_order_success(self, courier, order):
        login, password, courier_id = courier
        track = order
        order_id = get_order_id(track)
        assert order_id is not None
        # Принять заказ
        accept_response = accept_order(order_id, courier_id)
        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}

    @allure.step('Принять заказ без id курьера')
    def test_accept_order_no_courier(self, order):
        track = order
        order_id = get_order_id(track)
        assert order_id is not None
        # Принять без courierId
        response = requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/' + str(order_id))
        assert response.status_code == 400

    @allure.step('Принять заказ с неправильным id курьера')
    def test_accept_order_wrong_courier(self, order):
        track = order
        order_id = get_order_id(track)
        assert order_id is not None
        # Принять с неправильным courierId
        response = requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/' + str(order_id), params={'courierId': 999999})
        assert response.status_code == 404

    @allure.step('Принять заказ без id заказа')
    def test_accept_order_no_order(self, courier):
        login, password, courier_id = courier
        # Принять без id заказа
        response = requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/', params={'courierId': courier_id})
        assert response.status_code == 404

    @allure.step('Принять заказ с неправильным id заказа')
    def test_accept_order_wrong_order(self, courier):
        login, password, courier_id = courier
        # Принять с неправильным id заказа
        response = requests.put('https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/999999', params={'courierId': courier_id})
        assert response.status_code == 404