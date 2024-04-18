from django.shortcuts import render
from .models import *

# Create your views here.
def HomePage(requests):
    return render(requests,"base.html")
def ShopPage(requests):
    susha=Sushi.objects.all()
    return render(requests,"shop.html",{"susha":susha})
def BasketPage(requests):
    return render(requests,"basket.html")
def AboutUsPage(requests):
    return render(requests,"about us.html")
def SettingsPage(requests):
    return render(requests,"settings.html")
