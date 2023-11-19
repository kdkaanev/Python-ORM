

from django.core.exceptions import ValidationError
import re

def validate_phone_number(value: str):
    if not re.match(r'^\+359\d{9}$', value):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")

def validate_name(value: str):
    for char in value:
        if not char.isalpha() or char.isspace():
            raise ValidationError("Name can only contain letters and spaces")