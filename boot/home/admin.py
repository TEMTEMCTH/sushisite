from django.contrib import admin

# Register your models here.
from .models import Sushi
@admin.register(Sushi)
class SushiAdmin(admin.ModelAdmin):
    list_display = ('name','img','price' )