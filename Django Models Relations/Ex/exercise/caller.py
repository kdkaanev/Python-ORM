import os


import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Artist, Song, Product, Review, DrivingLicense, Driver
from django.db.models import QuerySet, Avg

from main_app.models import Author, Book
from datetime import datetime, date, timedelta


# Create queries within functions
def show_all_authors_with_their_books() -> str:
    authors_with_books = []
    authors = Author.objects.all().order_by('id')
    for author in authors:
        books = Book.objects.filter(author=author)
        if not books:
            continue

        titles = ', '.join([book.title for book in books])
        authors_with_books.append(f'{author.name} has written - {titles}!')

    return '\n'.join(authors_with_books)


def delete_all_authors_without_books() -> None:
    authors_without_books = Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Artist]:
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.review_set.all()
    total_rating = sum(r.rating for r in reviews)
    average_rating = total_rating / reviews.count()

    return average_rating


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    reviews = Review.objects.filter(rating__gte=threshold)
    return reviews


def get_products_with_no_reviews() -> QuerySet[Product]:
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    return Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() ->str:
    licenses = DrivingLicense.objects.all().order_by('-licence      -number')

    return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date):
    expiration_date = due_date - timedelta(days=365)
    expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_date)

    return expired_drivers


# Get drivers with expired licenses
drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
for driver in drivers_with_expired_licenses:
    print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")
