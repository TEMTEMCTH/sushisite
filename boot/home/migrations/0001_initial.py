# Generated by Django 5.0.4 on 2024-04-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sushi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
    ]