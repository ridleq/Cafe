from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table_number', 'items']
        widgets = {
            'items': forms.CheckboxSelectMultiple(),
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
