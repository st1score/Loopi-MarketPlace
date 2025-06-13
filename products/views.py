from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from user.forms import RegistrationForm
from .cart import Cart
from django.db.models import Q
from .models import CartItem
from decimal import Decimal


# --- Регистрация ---
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'products/registration.html', {'form': form})


# --- Товары ---
def index(request):
    return render(request, 'products/index.html')

def product_list(request):
    query = request.GET.get('q')  # Получаем поисковый запрос из формы
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'products/product_list.html', {'products': products, 'query': query})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


# --- Корзина через класс Cart ---
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['quantity'] += 1  # <- увеличиваем количество
    else:
        cart[product_id] = {'quantity': 1}  # <- создаём словарь с quantity

    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})

    # 💡 Исправляем старый формат корзины (int -> dict)
    for key in list(cart.keys()):
        if isinstance(cart[key], int):
            cart[key] = {'quantity': cart[key]}
    request.session['cart'] = cart

    cart_items = []
    total_price = Decimal('0.00')

    for product_id, item in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        quantity = item['quantity']
        total = product.price * quantity
        total_price += total

        cart_items.append({
            'product_id': product_id,
            'product': product,
            'quantity': quantity,
            'total_price': total,
        })

    context = {
        'cart': cart_items,
        'total_price': total_price,
    }
    return render(request, 'products/cart.html', context)

from django.views.decorators.http import require_POST

@require_POST
def update_cart_quantity(request, item_id):
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if str(item_id) in cart:
            cart[str(item_id)]['quantity'] = new_quantity
            request.session['cart'] = cart

    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('view_cart')

# def clear_cart(request):
#     request.session['cart'] = {}
#     return redirect('view_cart')

