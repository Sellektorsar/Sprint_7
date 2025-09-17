BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

# Эндпоинты API
COURIER_URL = BASE_URL + 'courier'
COURIER_LOGIN_URL = BASE_URL + 'courier/login'
ORDERS_URL = BASE_URL + 'orders'

# Тестовые данные заказа по умолчанию
ORDER_DATA = {
    "firstName": "Test",
    "lastName": "User",
    "address": "Test Address 123",
    "metroStation": 1,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2023-06-06",
    "comment": "Test comment",
    "color": []
}

# Сообщения об ошибках
ERROR_MISSING_DATA = "Недостаточно данных для создания учетной записи"
ERROR_DUPLICATE_LOGIN = "Этот логин уже используется. Попробуйте другой."
ERROR_LOGIN_FAILED = "Учетная запись не найдена"
ERROR_MISSING_LOGIN_DATA = "Недостаточно данных для входа"
ERROR_MISSING_COURIER_ID = "Недостаточно данных для поиска"
ERROR_COURIER_NOT_FOUND = "Курьера с таким id не существует"
ERROR_ORDER_NOT_FOUND = "Заказа с таким id не существует"
# В некоторых ручках текст отличается (короткая форма)
ERROR_COURIER_NOT_FOUND_SHORT = "Курьера с таким id нет."