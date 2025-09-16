import pytest
import requests
import allure

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

class TestOrderCreation:

    @pytest.mark.parametrize("color", [
        [],
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ])
    @allure.step('Создать заказ с цветом: {color}')
    def test_create_order(self, color):
        payload = {
            "firstName": "Test",
            "lastName": "User",
            "address": "Test Address 123",
            "metroStation": 1,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2023-06-06",
            "comment": "Test comment",
            "color": color
        }
        response = requests.post(BASE_URL + 'orders', json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()