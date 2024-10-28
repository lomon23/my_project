from django.contrib.auth.models import AbstractUser
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image_url = models.URLField(max_length=200, blank=True)  # Поле для URL зображення

    def __str__(self):
        return self.name
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Посилання на товар
    customer_name = models.CharField(max_length=100)  # Ім'я покупця
    customer_email = models.EmailField()  # Email покупця
    card_number = models.CharField(max_length=16)  # Номер картки
    order_date = models.DateTimeField(auto_now_add=True)  # Дата замовлення

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"













