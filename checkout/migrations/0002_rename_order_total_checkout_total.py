# Generated by Django 3.2 on 2022-10-16 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='order_total',
            new_name='total',
        ),
    ]