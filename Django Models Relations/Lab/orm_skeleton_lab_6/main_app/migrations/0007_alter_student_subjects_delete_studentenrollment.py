# Generated by Django 4.2.4 on 2023-11-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_studentenrollment_enrollment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(to='main_app.subject'),
        ),
        migrations.DeleteModel(
            name='StudentEnrollment',
        ),
    ]
