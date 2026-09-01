# QA Autotests — Python + Pytest

Проект с автоматизированными API и UI-тестами на Python.

## О проекте

Проект создан для демонстрации практического подхода к автоматизации тестирования.

Количество тестов ограничено для демонстрации основных подходов. В реальном проекте набор сценариев может быть значительно больше и расширяется в зависимости от требований и сложности системы.

Проект отражает мой текущий практический опыт в автоматизации и не является полноценным production-ready framework.

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

* Создание и получение пользователя
* Валидация email, имени и возраста
* Дубликаты пользователей
* HTTP status code и JSON-ответы
* Граничные значения и классы эквивалентности

### UI

* Открытие главной страницы GoodFon
* Проверка элементов страницы
* Поиск обоев
* Проверка результатов поиска
* Переход на страницу авторизации

### E2E

* Создание пользователя через API
* Проверка данных в PostgreSQL
* Проверка отсутствия дубликатов в БД

## Подход

* AAA: Arrange, Act, Assert
* Pytest fixtures
* Pytest markers
* Page Object для UI-тестов
* Параметризованные тесты
* SQL-проверки PostgreSQL

## Структура

```text
my_api_autotests/
├── api_tests/
│   ├── positive_tests/
│   ├── negative_tests/
│   └── e2e_tests/
├── tests/
│   └── ui_tests/
│       └── pages/
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

.env`, `venv` и служебные файлы не загружаются в репозиторий благодаря `.gitignore`.
