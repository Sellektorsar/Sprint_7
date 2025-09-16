import requests
import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'

# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(BASE_URL + 'courier', json=payload)
    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    # возвращаем список
    return login_pass

def delete_courier(courier_id):
    response = requests.delete(BASE_URL + f'courier/{courier_id}')
    return response

def create_order(color=None):
    payload = {
        "firstName": "Test",
        "lastName": "User",
        "address": "Test Address 123",
        "metroStation": 1,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2023-06-06",
        "comment": "Test comment",
        "color": color or []
    }
    response = requests.post(BASE_URL + 'orders', json=payload)
    if response.status_code == 201:
        return response.json()['track']
    return None

def get_order_id(track):
    response = requests.get(BASE_URL + 'orders/track', params={'t': track})
    if response.status_code == 200:
        return response.json()['order']['id']
    return None

def accept_order(order_id, courier_id):
    response = requests.put(BASE_URL + f'orders/accept/{order_id}', params={'courierId': courier_id})
    return response