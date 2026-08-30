# API Autotests — Python + Pytest

Небольшой учебный проект с API-автотестами на Python.

Цель проекта — продемонстрировать мой подход к автоматизации тестирования: структура тестов по AAA, использование фикстур, параметризованные SQL-запросы и проверки взаимодействия API с PostgreSQL.

## Стек

* Python
* Pytest
* Requests
* PostgreSQL
* psycopg2
* Docker
* python-dotenv

## Что тестируется

### Positive API tests

* Создание пользователя — `POST /users`
* Проверка статус-кода и тела ответа

### Negative API tests

* Создание пользователя с дублирующимся email
* Невалидный email
* Невалидный возраст
* Получение несуществующего пользователя

### E2E tests

Проверяется полный сценарий:

`API → PostgreSQL`

* Создание пользователя и проверка данных в БД
* Проверка отсутствия дубликата в БД

## Структура проекта

```text
my_api_autotests/
├── api_tests/
│   ├── test_api_positive.py
│   ├── test_api_negative.py
│   └── test_api_e2e.py
├── conftest.py
├── .gitignore
├── README.md
├── .env
└── venv/
```

## AAA

Тесты организованы по принципу:

* **Arrange** — подготовка данных и окружения
* **Act** — выполнение действия через API
* **Assert** — проверка результата

## Fixtures

В `conftest.py` находятся общие фикстуры:

* `base_url` — URL API
* `user_data` — тестовые данные пользователя
* `unique_email` — генерация уникального email
* `db_cursor` — подключение к PostgreSQL

## Запуск тестов

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить все тесты:

```bash
pytest -v
```

Запустить только API:

```bash
pytest api_tests/test_api_positive.py -v
pytest api_tests/test_api_negative.py -v
```

Запустить E2E:

```bash
pytest api_tests/test_api_e2e.py -v
```

## Результат

Все тесты проходят успешно.

> `.env` и виртуальное окружение `venv` не загружаются в репозиторий.
