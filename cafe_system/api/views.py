from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from order.models import Dish, Order
from .serializers import DishSerializer, OrderSerializer
from .utils import update_sum


# ViewSet для модели Dish
class DishViewSet(viewsets.ModelViewSet):
    """
    DishViewSet предоставляет CRUD-операции
    (создание, чтение, обновление, удаление)
    для модели Dish через API. Он автоматически
    обрабатывает запросы, такие как GET, POST, PUT, DELETE.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [AllowAny]


# Поиск для модели Order
class OrderFilter(filters.FilterSet):
    """
    OrderFilter используется для фильтрации (Поиска) запросов к модели Order.
    Позволяет фильтровать заказы по полям id и status.
    """
    status = filters.CharFilter(field_name='status', lookup_expr='exact')
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')

    class Meta:
        model = Order
        fields = ['id', 'status']


# ViewSet для модели Order
class OrderViewSet(viewsets.ModelViewSet):
    """
    OrderViewSet предоставляет CRUD-операции для модели Order через API.
    Также поддерживает фильтрацию заказов по полям id и status.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    def perform_create(self, serializer):
        """
        Переопределяем метод perform_create для подсчета общей суммы заказа.
        """
        order = serializer.save()
        update_sum(order)

    def perform_update(self, serializer):
        """
        Переопределяем метод perform_update для подсчета общей суммы заказа.
        """
        order = serializer.save()
        update_sum(order)
