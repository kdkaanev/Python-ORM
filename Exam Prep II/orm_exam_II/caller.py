import os
import django


# Set up Django
from django.db.models import Q,Count,F
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product


# Create and run your queries within functions
def get_profiles(self, search_string=None) -> str:
    if search_string is None:
        return ''
    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(email__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    return "\n".join(
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders.count()}"
        for p in profiles
    )


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    return '\n'.join(
        f'Profile: {p.full_name}, orders: {p.orders_count}'
        for p in profiles
    )


def get_last_sold_products() -> str:
    last_orders = Order.objects.prefetch_related('products').last()
    if last_orders is None or not last_orders.products.exists():
        return ''
    result = [product.name for product in last_orders.products.all()]
    return f"Last sold products: {', '.join(result)}"


print(get_profiles('fil'))
print(get_loyal_profiles())
print(get_last_sold_products())