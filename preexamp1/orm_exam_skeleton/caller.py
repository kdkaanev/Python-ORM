import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from django.db.models import Q, Count, Avg
# Import your models here
from main_app.models import *


# Create and run your queries within functions
def get_directors(search_name=None, search_nationality=None):
    directors = Director.objects.all()
    if not search_name and not search_nationality:
        return ("")
    if search_name:
        directors = Director.objects.filter(full_name__icontains=search_name)
    if search_nationality:
        directors = Director.objects.filter(nationality__icontains=search_nationality)
    elif search_name and search_nationality:
        directors = Director.objects.filter(
            Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality))
    if not directors:
        return ("")
    else:
        result = []
        for director in directors:
            result.append(
                f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}")

        return "\n".join(result)


def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()
    if not director:
        return ""
    return f"Top Director: {director.full_name}, movies: {director.movies_count}."


def get_top_actor():
    actors = Actor.objects.annotate(
        movies_count=Count('movies'),
        average_rating=Avg('movies__rating')
    ).order_by('-movies_count', 'full_name').first()

    if not actors or not actors.movies_count:
        return ""
    movie_title = ', '.join([movie.title for movie in actors.movies])
    return f"Top Actor: {actors.full_name}, starring in movies: {movie_title}, movies average rating: {actors.avgerage_rating}"

print(get_top_director())