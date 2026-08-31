# API Autotests — Python + Pytest

Небольшой учебный проект с API-автотестами на Python.

Цель проекта — продемонстрировать мой подход к автоматизации тестирования: структура тестов по AAA, использование pytest fixtures и markers, параметризованные SQL-запросы и проверки взаимодействия API с PostgreSQL.

## Стек

* Python
* Pytest
* Requests
* PostgreSQL
* psycopg2
* python-dotenv
* SQL

## Что тестируется

### Positive API tests

* Создание пользователя — `POST /users`
* Получение пользователя по ID — `GET /users/{id}`
* Проверка HTTP status code
* Проверка данных в JSON-ответе

### Negative API tests

* Создание пользователя с дублирующимся email
* Создание пользователя с невалидным email
* Создание пользователя с невалидным возрастом
* Получение несуществующего пользователя

### E2E tests

Проверяется взаимодействие:

`API → PostgreSQL`

* Создание пользователя и проверка данных в БД
* Проверка отсутствия дубликата пользователя в БД

## Структура проекта

```text
my_api_autotests/
├── api_tests/
│   ├── test_api_positive.py
│   ├── test_api_negative.py
│   └── test_api_e2e.py
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md
```

## AAA

Тесты организованы по принципу AAA:

* **Arrange** — подготовка данных и окружения
* **Act** — выполнение действия через API
* **Assert** — проверка результата

## Fixtures

В `conftest.py` находятся общие фикстуры:

* `base_url` — базовый URL API
* `user_data` — тестовые данные пользователя
* `unique_email` — генерация уникального email
* `db_cursor` — подключение к PostgreSQL

## Pytest markers

Для категоризации API-тестов используется marker:

`@pytest.mark.api`

## Запуск тестов

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить все тесты:

```bash
pytest -v
```

Запустить Positive API tests:

```bash
pytest api_tests/test_api_positive.py -v
```

Запустить Negative API tests:

```bash
pytest api_tests/test_api_negative.py -v
```

Запустить E2E tests:

```bash
pytest api_tests/test_api_e2e.py -v
```

## Результат

На текущем этапе проект содержит 8 API-автотестов:

* 2 Positive
* 4 Negative
* 2 E2E

Все тесты проходят успешно.

> `.env`, виртуальное окружение `venv` и служебные файлы PyCharm/Pytest не загружаются в репозиторий благодаря `.gitignore`.

```
```
