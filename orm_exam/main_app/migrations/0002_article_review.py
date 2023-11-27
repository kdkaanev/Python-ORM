# Generated by Django 4.2.4 on 2023-11-26 07:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5)])),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('category', models.CharField(choices=[('Technology', 'Technology'), ('Science', 'Science'), ('Education', 'Education')], default='Technology', max_length=10)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('authors', models.ManyToManyField(to='main_app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_article', to='main_app.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_author', to='main_app.author')),
            ],
        ),
    ]