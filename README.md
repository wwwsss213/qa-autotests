# QA Autotests — Python + Pytest

Проект с автоматизированными тестами API и UI на Python.

## Стек

* Python
* Pytest
* Requests
* Playwright
* PostgreSQL
* psycopg2
* python-dotenv
* SQL

## Что тестируется

### API

* Создание пользователя
* Получение пользователя по ID
* Валидация email, имени и возраста
* Дубликаты пользователей
* Проверка HTTP status code и JSON-ответов
* Проверки граничных значений и классов эквивалентности

### UI

* Открытие главной страницы GoodFon
* Проверка элементов страницы
* Поиск обоев
* Проверка отображения результатов поиска

### E2E

* Создание пользователя через API
* Проверка данных в PostgreSQL
* Проверка отсутствия дубликатов в БД

## Структура

```text
my_api_autotests/
├── api_tests/
│   ├── positive_tests/
│   ├── negative_tests/
│   └── e2e_tests/
├── tests/
│   └── ui_tests/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Запуск

Все тесты:

```bash
pytest -v
```

API:

```bash
pytest -m api -v
```

UI:

```bash
pytest -m ui -v --headed
```

E2E:

```bash
pytest -m e2e -v
```

> `.env`, `venv` и служебные файлы не загружаются в репозиторий благодаря `.gitignore`.
