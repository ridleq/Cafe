from django.views.generic import (
    ListView, CreateView,
    DeleteView, UpdateView
)
from django.views import View
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.db.models import Sum

from .forms import OrderForm, StatusForm
from .models import Order


class IndexListView(ListView):
    "Запрос всех заказов на главной странице."
    model = Order
    paginate_by = 3
    template_name = 'order/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_revenue'] = Order.objects.filter(
            status='paid'
        ).aggregate(Sum('total_price'))['total_price__sum'] or 0
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort', '-id')
        if sort_by == 'status':
            return queryset.order_by('-status')
        return queryset.order_by('-id')


class OrderCreateView(CreateView):
    "Запрос создания заказа."
    model = Order
    form_class = OrderForm
    template_name = 'order/add_order.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        order = self.object
        total_price = order.items.aggregate(
            total_price=Sum('price')
        )['total_price']
        order.total_price = total_price
        order.save()
        return response

    def get_success_url(self):
        return reverse('order:index')


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/add_order.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        order = self.object
        total_price = order.items.aggregate(
            total_price=Sum('price')
        )['total_price']
        order.total_price = total_price
        order.save()
        return response

    def get_success_url(self):
        return reverse('order:index')


class OrderDeleteView(DeleteView):
    "Запрос удаления заказа."
    model = Order
    template_name = 'order/add_order.html'

    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(Order, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('order:index')


class StatusUpdateView(UpdateView):
    model = Order
    form_class = StatusForm
    template_name = 'order/edit_status.html'

    def get_success_url(self):
        return reverse('order:index')


class SerachView(View):
    template_name = 'order/search.html'

    status_map = {
        'в ожидании': 'waiting',
        'готово': 'ready',
        'оплачено': 'paid',
    }

    def get(self, request, *args, **kwargs):
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
