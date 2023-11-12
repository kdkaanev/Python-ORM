import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
from main_app.models import ZooDisplayAnimal

is_proxy = ZooDisplayAnimal._meta.proxy

if is_proxy:
    print("ZooDisplayAnimal is a proxy model.")
else:
    print("ZooDisplayAnimal is not a proxy model.")
