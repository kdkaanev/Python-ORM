import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Artist, Song


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

    # Create artists


artist1 = Artist.objects.create(name="Daniel Di Angelo")
artist2 = Artist.objects.create(name="Indila")

# Create songs
song1 = Song.objects.create(title="Lose Face")
song2 = Song.objects.create(title="Tourner Dans Le Vide")
song3 = Song.objects.create(title="Loyalty")

# Add a song to an artist
add_song_to_artist("Daniel Di Angelo", "Lose Face")
add_song_to_artist("Daniel Di Angelo", "Loyalty")
add_song_to_artist("Indila", "Tourner Dans Le Vide")

# Get all songs by a specific artist
songs = get_songs_by_artist("Daniel Di Angelo")
for song in songs:
    print(f"Daniel Di Angelo: {song.title}")

# Get all songs by a specific artist
songs = get_songs_by_artist("Indila")
for song in songs:
    print(f"Indila: {song.title}")

# Remove a song from an artist
remove_song_from_artist("Daniel Di Angelo", "Lose Face")

# Check if the song is removed
songs = get_songs_by_artist("Daniel Di Angelo")

for song in songs:
    print(f"Songs by Daniel Di Angelo after removal: {song.title}")
