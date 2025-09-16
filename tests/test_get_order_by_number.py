import requests
import allure
from data import ORDERS_URL

class TestGetOrderByNumber:

    @allure.title('Получить заказ по треку успешно')
    def test_get_order_success(self, order):
        track = order
        # Получить заказ
        response = requests.get(ORDERS_URL + '/track', params={'t': str(track)})
        assert response.status_code == 200
        data = response.json()
        assert 'order' in data

    @allure.title('Получить заказ без номера трека')
    def test_get_order_no_track(self):
        response = requests.get(ORDERS_URL + '/track')
        assert response.status_code == 400
        data = response.json()
        # Parse response

    @allure.title('Получить заказ с неправильным номером трека')
    def test_get_order_wrong_track(self):
        response = requests.get(ORDERS_URL + '/track', params={'t': 'wrongtrack'})
        assert response.status_code == 500
        # API returns 500 for wrong track