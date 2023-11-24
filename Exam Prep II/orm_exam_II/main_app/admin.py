from django.contrib import admin

from main_app.models import Profile, Product, Order


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['full_name', 'email', 'phone_number', 'is_active']
    search_fields = ['full_name ', 'email']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'in_stock', 'is_available']
    list_filter = ['is_available']
    search_fields = ['name ']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['profile', 'total_price', 'creation_date', 'is_completed']
    list_filter = ['is_completed']
    search_fields = ['profile__full_name ']
