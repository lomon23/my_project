from django.shortcuts import render, get_object_or_404,redirect
from .models import Order, Product
from .forms import OrderForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Сторінка конкретного товару
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
from .forms import ProductForm

# Додавання нового товару
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product  # Прив'язка замовлення до товару
            order.save()
            print("Order successfully placed!")  # Додано для відлагодження
            return redirect('product_detail', product_id=product.id)  # Повертаємося на сторінку товару
        else:
            print("Form is not valid")  # Додано для відлагодження
    else:
        form = OrderForm()

    return render(request, 'order_product.html', {'form': form, 'product': product})

def contact(request):
    return render(request, 'contact.html')  # Вказуємо, який шаблон повертати

def about(request):
    return render(request, 'about.html')