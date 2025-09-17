import requests
import allure
from data import ORDERS_URL

class TestOrdersList:

    @allure.title('Получить список заказов')
    def test_get_orders_list(self):
        response = requests.get(ORDERS_URL)
        assert response.status_code == 200
        data = response.json()
        assert 'orders' in data
        assert isinstance(data['orders'], list)