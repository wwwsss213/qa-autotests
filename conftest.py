import os
import random
import pytest
import psycopg2
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Возвращает базовый URL для API из .env"""
    return os.getenv("API_BASE_URL")


@pytest.fixture
def unique_email():
    """Генерирует случайный уникальный email для каждого теста"""
    return f"user{random.randint(10000, 99999)}@example.com"


@pytest.fixture
def user_data(unique_email):
    """Формирует словарь с данными пользователя для отправки в POST запрос"""
    return {
        "name": "Test Test",
        "email": unique_email,
        "age": 35
    }


@pytest.fixture(scope="function")
def db_cursor():
    """Подключается к PostgreSQL в Docker через доступы из .env.

    После завершения теста автоматически закрывает соединение.
    """
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    # Включаем автокоммит, чтобы изменения в базе (если они будут) сразу сохранялись
    connection.autocommit = True
    cursor = connection.cursor()

    yield cursor  # Передаем курсор в тест

    # Блок Clean Up (выполняется строго ПОСЛЕ теста)
    cursor.close()
    connection.close()
