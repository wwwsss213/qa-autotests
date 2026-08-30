import os
import random

import pytest
import psycopg2
import requests
from dotenv import load_dotenv


# Загружаем переменные из .env файла
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Возвращает базовый URL для API из .env."""
    return os.getenv("API_BASE_URL")


@pytest.fixture
def api_client():
    """Создаёт HTTP-клиент для API-запросов."""
    session = requests.Session()
    session.trust_env = False
    return session


@pytest.fixture
def unique_email():
    """Генерирует случайный уникальный email для каждого теста."""
    return f"user{random.randint(10000, 99999)}@example.com"


@pytest.fixture
def user_data(unique_email):
    """Формирует данные пользователя для POST-запроса."""
    return {
        "name": "Test Test",
        "email": unique_email,
        "age": 35
    }


@pytest.fixture(scope="function")
def db_cursor():
    """Подключается к PostgreSQL в Docker через данные из .env.

    После завершения теста автоматически закрывает соединение.
    """
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    connection.autocommit = True
    cursor = connection.cursor()

    yield cursor

    cursor.close()
    connection.close()