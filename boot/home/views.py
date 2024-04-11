from django.shortcuts import render

# Create your views here.
def HomePage(requests):
    return render(requests,"base.html")
def ShopPage(requests):
    return render(requests,"shop.html")
def BasketPage(requests):
    return render(requests,"basket.html")
def AboutUsPage(requests):
    return render(requests,"about us.html")
def SettingsPage(requests):
    return render(requests,"settings.html")
