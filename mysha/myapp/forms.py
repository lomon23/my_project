from django import forms
from .models import Product
from .models import Order



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'description', 'image_url']  # Додаємо image_url
class OrderForm(forms.ModelForm):
    card_number = forms.CharField(widget=forms.PasswordInput)  # Маскуємо введення номеру картки

    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'card_number']



