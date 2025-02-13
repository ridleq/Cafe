from rest_framework import serializers

from order.models import Dish, Order


# Сериализатор для модели Dish.
class DishSerializer(serializers.ModelSerializer):
    """
    DishSerializer используется для преобразования объектов
    модели Dish в формат JSON и обратно. Это упрощает работу
    с данными, передаваемыми через API.
    """
    class Meta:
        model = Dish
        fields = ['id', 'name', 'price']


# Сериализатор для модели Order.
class OrderSerializer(serializers.ModelSerializer):
    """
    OrderSerializer используется для преобразования объектов модели Order
    в формат JSON и обратно. Он также включает связанные объекты Dish
    через поле items.
    """
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Dish.objects.all()
    )

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']
