import requests
import allure

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

class TestOrdersList:

    @allure.step('Получить список заказов')
    def test_get_orders_list(self):
        response = requests.get(BASE_URL + 'orders')
        assert response.status_code == 200
        data = response.json()
        assert 'orders' in data
        assert isinstance(data['orders'], list)