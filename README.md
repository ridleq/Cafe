# Система управления заказами в кафе

[Автор: Дмитрий](https://github.com/ridleq)

Система управления заказами в кафе - это веб-приложение, созданное для управления заказами в кафе.

## Функционал приложения:

- Пользователь может создавать заказ 
- Пользователь может редактировать список блюд в заказе
- Пользователь может удалять заказ
- Пользователь может изменять статус заказа (В ожидании/Готов/Оплачен)
- Поиск заказа по 2 параметрам: по ID или статусу
- Вывод всех заказов с их ID, номером стола, списком блюд, общей стоимостью заказа и статусом

### Как запустить приложение локально:

```
1. Клонировать репозиторий и перейти в него в командной строке:
    git clone git@github.com:ridleq/Cafe.git
```

```
2. cd ~/Cafe
```

```
3. Создать виртуальное окружение:
    - Linux/macOS: python3 -m venv venv
    - Windows: python -m venv venv или py -3 -m venv venv
```

```
4. Активировать виртуальное окружение:
    - Linux/macOS: source venv/bin/activate
    - Windows: source venv/Scripts/activate
```

```
5. Установить библиотеки командой:
    pip install -r requirements.txt
```

```
6. cd ~/cafe_system
```

```
7. Выполнить миграции:
    python manage.py migrate 
```

```
8. Запустить приложение:
    - Linux/macOS: python3 manage.py runserver
    - Windows: python manage.py runserver
```

### Перед запуском приложения необходимо произвести тестрирование.
Запуск тестов:

```
1. Переходим в корневую папку проекта - cd ~/library
```

```
2. Запускаем тесты командой - python -m tests.all_tests
```

```
3. Смотрим результаты
```


## Технологический стек приложения:
- [Python](https://www.python.org/)
- [Django](https://docs.djangoproject.com/)
- [HTML/CSS](https://www.w3schools.com/)
- [SQLite](https://www.sqlite.org/docs.html)
- [pytest](https://docs.pytest.org/en/stable/)