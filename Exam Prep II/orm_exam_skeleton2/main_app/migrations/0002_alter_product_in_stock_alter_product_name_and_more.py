# Generated by Django 4.2.4 on 2023-11-23 17:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]