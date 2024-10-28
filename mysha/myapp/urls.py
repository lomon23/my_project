from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/buy/', views.order_product, name='order_product'),  # buy замість order
    path('add/', views.add_product, name='add_product'),
    path('contact/', views.contact, name='contact'),  # додайте цей рядок
    path('about/', views.about, name='about'),

]