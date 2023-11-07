import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Artist, Song, Product, Review
from django.db.models import QuerySet, Avg


# from main_app.models import Author, Book
#
#
# # Create queries within functions
# def show_all_authors_with_their_books() -> str:
#     authors_with_books = []
#     authors = Author.objects.all().order_by('id')
#     for author in authors:
#         books = Book.objects.filter(author=author)
#         if not books:
#             continue
#
#         titles = ', '.join([book.title for book in books])
#         authors_with_books.append(f'{author.name} has written - {titles}!')
#
#     return '\n'.join(authors_with_books)
#
#
# def delete_all_authors_without_books() -> None:
#     authors_without_books = Author.objects.filter(book__isnull=True).delete()


# def add_song_to_artist(artist_name: str, song_title: str):
#     artist = Artist.objects.get(name=artist_name)
#     song = Song.objects.get(title=song_title)
#
#     artist.songs.add(song)
#
#
# def get_songs_by_artist(artist_name: str) -> QuerySet[Artist]:
#     artist = Artist.objects.get(name=artist_name)
#     return artist.songs.all().order_by('-id')
#
#
# def remove_song_from_artist(artist_name: str, song_title: str):
#
#     artist = Artist.objects.get(name=artist_name)
#     song = Song.objects.get(title=song_title)
#
#     artist.songs.remove(song)
#
def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.filter(rating__isnull=False)
    if reviews.count() == 0:
        return 0
    return reviews.aggregate(average_rating=Avg('rating'))['average_rating']



def get_reviews_with_high_ratings(threshold: int):
    reviews = Review.objects.filter(rating__gte=threshold)
    return reviews

def get_products_with_no_reviews(product_name: str):

    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    if reviews.count() == 0:
        return product.ordered_by('-name')
    return None

def delete_products_without_reviews():

    products_without_reviews = Product.objects.filter(reviews__isnull=True).delete()














