import requests
import allure

class TestGetOrderByNumber:

    @allure.step('Получить заказ по треку успешно')
    def test_get_order_success(self, order):
        track = order
        # Получить заказ
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track', params={'t': track})
        assert response.status_code == 200
        assert 'order' in response.json()

    @allure.step('Получить заказ без номера трека')
    def test_get_order_no_track(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track')
        assert response.status_code == 400

    @allure.step('Получить заказ с неправильным номером трека')
    def test_get_order_wrong_track(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track', params={'t': 'wrongtrack'})
        assert response.status_code == 500  # API возвращает 500 для неправильного трека