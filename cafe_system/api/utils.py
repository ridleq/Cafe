from django.db.models import Sum


def update_sum(order):
    total_price = order.items.aggregate(
        total_price=Sum('price')
    )['total_price']
    order.total_price = total_price
    order.save()
