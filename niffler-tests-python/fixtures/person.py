"""
    Фикстуры генерации тестового пользователя
"""
import pytest
from mimesis import Person


@pytest.fixture()
def person_generator():
    """
    Генератор человека
    """
    return Person('ru')


@pytest.fixture()
def user_data(person_generator):
    """
    :return: возвращает тестовые данные для регистрации пользователя
    """
    password = person_generator.password()
    data = {
        "username": person_generator.username(),
        "password": password,
        "submit_password": password,
        "first_name": person_generator.first_name()
    }
    return data
