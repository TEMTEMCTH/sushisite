# Generated by Django 5.0.4 on 2024-04-18 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sushi',
            old_name='descriptions',
            new_name='Name',
        ),
    ]
