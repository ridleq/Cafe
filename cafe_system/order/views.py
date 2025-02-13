from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import OrderForm, StatusForm
from .models import Order


# Представление для отображения списка заказов на главной странице.
class IndexListView(ListView):
    """
    IndexListView отображает список всех заказов на главной странице.
    Реализована пагинация и возможность сортировки.
    """
    model = Order
    paginate_by = 3
    template_name = 'order/index.html'

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст данные о суммарной выручке от оплаченных заказов.
        """
        context = super().get_context_data(**kwargs)
        context['total_revenue'] = Order.objects.filter(
            status='paid'
        ).aggregate(Sum('total_price'))['total_price__sum'] or 0
        return context

    def get_queryset(self):
        """
        Возвращает отсортированный список заказов.
        Сортировка может быть по ID (по умолчанию) или по статусу.
        """
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', '-id')
        if sort_by == 'status':
            return queryset.order_by('-status')
        return queryset.order_by('-id')


# Представление для создания нового заказа.
class OrderCreateView(CreateView):
    """
    OrderCreateView позволяет создавать новый заказ.
    После создания автоматически рассчитывается общая стоимость заказа.
    """
    model = Order
    form_class = OrderForm
    template_name = 'order/add_order.html'

    def form_valid(self, form):
        """
        Вызывается при успешной валидации формы.
        Рассчитывает общую стоимость заказа на основе выбранных блюд.
        """
        response = super().form_valid(form)
        order = self.object
        total_price = order.items.aggregate(
            total_price=Sum('price')
        )['total_price']
        order.total_price = total_price
        order.save()
        return response

    def get_success_url(self):
        """
        Возвращает URL для перенаправления после успешного создания заказа.
        """
        return reverse('order:index')


# Представление для обновления существующего заказа.
class OrderUpdateView(UpdateView):
    """
    OrderUpdateView позволяет редактировать существующий заказ.
    После редактирования автоматически пересчитывается общая стоимость заказа.
    """
    model = Order
    form_class = OrderForm
    template_name = 'order/add_order.html'

    def form_valid(self, form):
        """
        Вызывается при успешной валидации формы.
        Пересчитывает общую стоимость заказа на основе обновленных данных.
        """
        response = super().form_valid(form)
        order = self.object
        total_price = order.items.aggregate(
            total_price=Sum('price')
        )['total_price']
        order.total_price = total_price
        order.save()
        return response

    def get_success_url(self):
        """
        Возвращает URL для перенаправления после успешного обновления заказа.
        """
        return reverse('order:index')


# Представление для удаления заказа.
class OrderDeleteView(DeleteView):
    """
    OrderDeleteView позволяет удалять существующий заказ.
    """
    model = Order
    template_name = 'order/add_order.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Проверяет, существует ли объект заказа перед удалением.
        """
        get_object_or_404(Order, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """
        Возвращает URL для перенаправления после успешного удаления заказа.
        """
        return reverse('order:index')


# Представление для изменения статуса заказа.
class StatusUpdateView(UpdateView):
    """
    StatusUpdateView позволяет изменять статус существующего заказа.
    """
    model = Order
    form_class = StatusForm
    template_name = 'order/edit_status.html'

    def get_success_url(self):
        """
        Возвращает URL для перенаправления после успешного изменения статуса.
        """
        return reverse('order:index')


# Представление для поиска заказов.
class SerachView(View):
    """
    SerachView позволяет искать заказы по ID или статусу.
    """
    template_name = 'order/search.html'

    # Словарь для преобразования статусов.
    status_map = {
        'в ожидании': 'waiting',
        'готово': 'ready',
        'оплачено': 'paid',
    }

    def get(self, request, *args, **kwargs):
        """
        Обрабатывает GET-запросы для поиска заказов.
        """
        query = request.GET.get('q', '')
        orders = Order.objects.none()
        if query:
            normal_query = query.strip().lower()
            if normal_query in self.status_map:
                normal_query = self.status_map[normal_query]
            if normal_query.isdigit():
                orders = Order.objects.filter(id=int(normal_query))
            else:
                orders = Order.objects.filter(
                    status__icontains=normal_query
                )

        context = {
            'orders': orders,
            'query': query,
        }
        return render(request, self.template_name, context)
