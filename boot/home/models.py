from django.db import models
from django.contrib.auth.models import User

class Sushi(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    price = models.FloatField()  # Изменяем тип на DecimalField

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sushi = models.ForeignKey(Sushi, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.sushi.price

    def __str__(self):
        return f"{self.quantity} x {self.sushi.name}"
