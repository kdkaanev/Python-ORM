# Generated by Django 4.2.4 on 2023-11-19 07:16

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, validators=[main_app.models.validate_name]),
        ),
    ]
