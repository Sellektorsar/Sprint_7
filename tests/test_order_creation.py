import pytest
import requests
import allure
from data import ORDERS_URL, ORDER_DATA


class TestOrderCreation:

    @pytest.mark.parametrize("color", [
        [],
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ])
    @allure.title('Создать заказ (параметризовано по цвету)')
    def test_create_order(self, color):
        payload = ORDER_DATA.copy()
        payload['color'] = color
        response = requests.post(ORDERS_URL, json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()