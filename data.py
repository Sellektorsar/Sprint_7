BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

# URLs
COURIER_URL = BASE_URL + 'courier'
COURIER_LOGIN_URL = BASE_URL + 'courier/login'
ORDERS_URL = BASE_URL + 'orders'

# Test data
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

# Response messages
ERROR_MISSING_DATA = "Недостаточно данных для создания учетной записи"
ERROR_DUPLICATE_LOGIN = "Этот логин уже используется. Попробуйте другой."
ERROR_LOGIN_FAILED = "Учетная запись не найдена"
ERROR_MISSING_LOGIN_DATA = "Недостаточно данных для входа"