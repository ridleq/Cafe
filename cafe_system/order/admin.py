from django.contrib import admin

from .models import Dish, Order


# Настройки админ-панели для модели Order.
class OrderAdmin(admin.ModelAdmin):
    """
    OrderAdmin определяет, как модель Order будет отображаться
    в админ-панели Django.
    """
    list_display = (
        'table_number',
        'total_price',
        'status'
    )


# Настройки админ-панели для модели Dish.
class DishAdmin(admin.ModelAdmin):
    """
    DishAdmin определяет, как модель Dish будет отображаться
    в админ-панели Django.
    """

    list_display = (
        'name',
        'price'
    )


# Регистрация моделей в админ-панели.
admin.site.register(Order, OrderAdmin)
admin.site.register(Dish, DishAdmin)
