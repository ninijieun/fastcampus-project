# Generated by Django 4.0.6 on 2022-09-19 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OrdersFood',
            new_name='Orderfood',
        ),
    ]
