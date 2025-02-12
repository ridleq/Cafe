from django.contrib import admin
from .models import Order
from .models import Dish


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'table_number',
        'total_price',
        'status'
    )


class DishAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price'
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(Dish, DishAdmin)
