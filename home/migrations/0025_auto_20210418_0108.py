# Generated by Django 3.1.6 on 2021-04-17 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_reserve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersupply',
            name='order',
        ),
        migrations.RemoveField(
            model_name='ordersupply',
            name='supply',
        ),
        migrations.RemoveField(
            model_name='ordersupply',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reserve',
            name='supply',
        ),
        migrations.RemoveField(
            model_name='reserve',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderSupply',
        ),
        migrations.DeleteModel(
            name='Reserve',
        ),
    ]
