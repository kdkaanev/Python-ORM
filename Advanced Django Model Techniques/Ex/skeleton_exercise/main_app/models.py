from django.core.exceptions import ValidationError
from django.db import models
from django.core import validators
# Create your models here.
def validate_name(value: str):
    if not value.isalpha() or not value.isspace():
        raise ValidationError("Name can only contain letters and spaces")

def validate_phone_number(value: str):
    code = "+359"
    if value[:4] != code and len(value) != 13:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_name]
    )
    age = models.PositiveIntegerField(
        validators=[validators.MinValueValidator(18, "Age must be greater than 18")]
    )
    email = models.EmailField(
        validators=[validators.EmailValidator("Enter a valid email address")]
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[validate_phone_number],
    )
    website_url = models.URLField(
        validators=[validators.URLValidator("Enter a valid URL")]
    )