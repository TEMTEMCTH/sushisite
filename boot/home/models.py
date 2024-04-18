from django.db import models

# Create your models here.

class Sushi(models.Model):
    Name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    def __str__(self):return self.Name

    