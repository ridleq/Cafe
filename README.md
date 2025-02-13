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

### Предоставлен API для работы с заказами

```
Для модели "Блюдо" доступно:
    - Создание (Post)
        ~/api/dishes/

    - Удаление (Delete)
        ~/api/dishes/

    - Вывод всех блюд (Get)
        ~/api/dishes/
```

```
Для модели "Заказ" доступно:
    - Создание (Post)
        ~/api/orders/

    - Редактирование списка блюд (Patch)
        ~/api/orders/ID/
    
    - Удаление (Delete)
        ~/api/orders/ID/
    
    - Изменение статуса (Patch)
        ~/api/orders/ID/
    
    - Поиск по ID и статусу (Get)
        ~/api/orders/?id=1
        ~/api/orders/?status=waiting

    - Вывод всех заказов (Get)
        ~/api/orders/
```

## Технологический стек приложения:
- [Python](https://www.python.org/)
- [Django](https://docs.djangoproject.com/)
- [HTML/CSS](https://www.w3schools.com/)
- [SQLite](https://www.sqlite.org/docs.html)
- [pytest](https://docs.pytest.org/en/stable/)
