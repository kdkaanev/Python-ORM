import os
from datetime import date

import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
# Create instances of RealEstateListing with locations
from main_app.models import RealEstateListing, VideoGame, Invoice, BillingInfo, Programmer, Project, Technology, Task, \
    Exercise

# Create task instances with custom creation dates
