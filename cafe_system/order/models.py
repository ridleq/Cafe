from django.db import models

from .utils import STATUS


# Определение модели Order.
class Order(models.Model):
    """
    Модель Order представляет заказ в системе. Она включает
    информацию о номере стола, связанных блюдах, общей стоимости
    и статусе заказа.
    """
    table_number = models.PositiveIntegerField(
        verbose_name='Номер стола',
    )
    items = models.ManyToManyField(
        'Dish',
        related_name='orders',
        verbose_name='Блюда в заказе'
    )
    total_price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        verbose_name='Общая сумма заказа',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        verbose_name='Статус',
        default='waiting'
    )


# Определение модели Dish.
class Dish(models.Model):
    """
    Модель Dish представляет блюдо в системе. Она включает
    информацию о названии и цене блюда.
    """
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )

    def __str__(self):
        """
        Метод, возвращающий строковое представление объекта Dish.
        Используется для отображения названия блюда в админ-панели
        и других местах.
        """
        return self.name
