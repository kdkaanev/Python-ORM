from django.db import models
from datetime import date

MONTHS = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'Junny'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December')
]
CITY = [
    ('sof', "Sofia"),
    ('pl', "Plovdiv"),
    ('bur', "Burgas"),
    ('var', "Varna")
]


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_day = models.DateField()
    work_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)



class Department(models.Model):
    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField("Employees Count", default=1)
    location = models.CharField(max_length=20, choices=CITY, null=True, blank=True)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_in_days = models.PositiveIntegerField(verbose_name="Duration in Days", null=True, blank=True)
    estimated_hours = models.FloatField(verbose_name="Estimated Hours", null=True, blank=True)
    start_date = models.DateField(verbose_name="Start Date", default=date.today, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)
