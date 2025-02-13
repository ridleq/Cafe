from django import forms

from .models import Order


# Форма для создания или редактирования заказа.
class OrderForm(forms.ModelForm):
    """
    OrderForm используется для создания и редактирования
    объектов модели Order. Она включает поля для номера
    стола и связанных блюд.
    """
    class Meta:
        model = Order
        fields = ['table_number', 'items']
        widgets = {
            'items': forms.CheckboxSelectMultiple(),
        }


# Форма для изменения статуса заказа.
class StatusForm(forms.ModelForm):
    """
    StatusForm используется для изменения статуса существующего
    заказа. Она включает только поле для статуса.
    """
    class Meta:
        model = Order
        fields = ['status']
