from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from order.models import Order, Dish
from .serializers import OrderSerializer, DishSerializer
from .utils import update_sum


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [AllowAny]


class OrderFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='exact')
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model = Order
        fields = ['id', 'status']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    def perform_create(self, serializer):
        order = serializer.save()
        update_sum(order)

    def perform_update(self, serializer):
        order = serializer.save()
        update_sum(order)
