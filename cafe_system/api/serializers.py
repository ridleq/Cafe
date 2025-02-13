from rest_framework import serializers
from order.models import Order, Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Dish.objects.all()
    )

    class Meta:
        model = Order
        fields = ['id', 'table_number', 'items', 'total_price', 'status']
