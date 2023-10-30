import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


# Import your models
# Create and check models
# Run and print your queries

def show_highest_rated_art():
    highest_rated = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{highest_rated.art_name} is the highest rated art with a {highest_rated.rating} rating!"


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    laptop = Laptop.objects.filter('price', 'id').first()
    return f"{laptop.brand} is the most expensive laptop available for  {laptop.price} $!"


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).exclude(storage=512).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).exclude(memory=16).update(memory=16)


def update_operation_systems():
    laptop = Laptop.objects.all()
    for l in laptop:
        if l.brand == "Apple":
            l.os = "MacOS"
        elif l.brand == "Asus":
            l.os = "Windows"
        elif l.brand == "Acer" or l.brand == "Acer":
            l.os = "Linux"
        elif l.brand == "Lenovo":
            l.os = "Chrome OS"
        l.save()


def delete_inexpencive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()
