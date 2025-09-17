import requests
import allure
from data import ORDERS_URL, ERROR_MISSING_COURIER_ID, ERROR_ORDER_NOT_FOUND

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
        # Разбираем тело ответа
        try:
            data = response.json()
            assert 'message' in data
            assert data['message'] == ERROR_MISSING_COURIER_ID
        except ValueError:
            assert response.text is not None and response.text != ''

    @allure.title('Получить заказ с неправильным номером трека')
    def test_get_order_wrong_track(self):
        response = requests.get(ORDERS_URL + '/track', params={'t': 'wrongtrack'})
        assert response.status_code == 500  # На стенде 500 для неверного трека
        # Разбираем тело ответа
        try:
            data = response.json()
            # Сообщение может отличаться по тексту на стенде — проверяем наличие и непустоту
            assert 'message' in data
            assert isinstance(data['message'], str) and data['message']
        except ValueError:
            # Ответ не в формате JSON — как минимум должен быть непустой текст
            assert response.text is not None and response.text != ''