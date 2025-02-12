from django.db import models

from .utils import STATUS


class Order(models.Model):
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


class Dish(models.Model):
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
        return self.name
