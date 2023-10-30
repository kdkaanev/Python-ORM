import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery


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



