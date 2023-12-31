# Generated by Django 4.2.4 on 2023-10-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_employee_month_of_employment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('employees_count', models.PositiveIntegerField(default=1, verbose_name='Employees Count')),
                ('location', models.CharField(choices=[('sof', 'Sofia'), ('pl', 'Plovdiv'), ('bur', 'Burgas'), ('var', 'Varna')], max_length=20)),
                ('last_edited_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
