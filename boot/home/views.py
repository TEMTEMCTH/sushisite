import json
from django.shortcuts import render
from .models import *

def HomePage(request):
    return render(request, "base.html")

def ShopPage(request):
    susha = Sushi.objects.all()
    return render(request, "shop.html", {"susha": susha})

def BasketPage(requests):
    # Получаем содержимое корзины из localStorage
    cart_items = json.loads(requests.session.get('cart', '[]'))

    # Вычисляем общую стоимость корзины
    total_price = sum(item['price'] for item in cart_items)

    # Передаем данные о корзине и общей стоимости в контекст шаблона
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(requests, "basket.html", context)

def AboutUsPage(request):
    return render(request, "about us.html")

def SettingsPage(request):
    return render(request, "settings.html")
