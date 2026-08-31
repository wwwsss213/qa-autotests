# API Autotests — Python + Pytest

Проект с API-автотестами на Python.

Цель — продемонстрировать подход к автоматизации API: AAA, Pytest fixtures и markers, параметризацию, проверки JSON и взаимодействие с PostgreSQL.

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
* Получение пользователя — `GET /users/{id}`
* Проверка status code и JSON
* Граничные значения `age`: `0–130`
* Валидная длина `name`: `2–100`
* Валидный формат `email`

### Negative API tests

* Дублирующийся email
* Невалидный email
* Отсутствующий email
* Невалидный `age`
* `age` вне диапазона `0–130`
* Невалидные типы `age` и `name`

### E2E

Проверяется взаимодействие:

`API → PostgreSQL`

* Создание пользователя и проверка данных в БД
* Проверка отсутствия дубликата

## Тест-дизайн

Используются:

* классы эквивалентности;
* граничные значения;
* positive / negative сценарии;
* проверка типов данных;
* параметризация `pytest.mark.parametrize`.

## Структура

```text
my_api_autotests/
├── api_tests/
│   ├── positive_tests/
│   └── negative_tests/
├── conftest.py
├── pytest.ini
├── .gitignore
└── README.md
```

## AAA

* **Arrange** — подготовка данных
* **Act** — запрос к API
* **Assert** — проверка результата

## Fixtures

* `base_url` — URL API
* `user_data` — данные пользователя
* `unique_email` — уникальный email
* `db_cursor` — подключение к PostgreSQL

## Запуск

```bash
pip install -r requirements.txt
pytest -v
```

Positive:

```bash
pytest api_tests/positive_tests -v
```

Negative:

```bash
pytest api_tests/negative_tests -v
```

## Результат

Текущая версия содержит:

* **16 Positive/E2E прогонов**
* **9 Negative прогонов**

Все тесты проходят успешно.

> `.env`, `venv` и служебные файлы не загружаются в репозиторий благодаря `.gitignore`.
