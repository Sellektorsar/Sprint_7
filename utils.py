import random
import string

# Утилиты для генерации тестовых данных


def generate_random_string(length):
    """Генерирует случайную строку из букв латинского алфавита в нижнем регистре указанной длины.
    Используется в тестах для создания уникальных логинов/паролей/имён курьеров.
    """
    letters = string.ascii_lowercase  # Набор допустимых символов (a-z)
    random_string = ''.join(random.choice(letters) for i in range(length))  # Сборка строки заданной длины
    return random_string