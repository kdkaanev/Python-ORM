import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal

from typing import List


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


def show_the_most_expensive_laptop() -> str:
    laptop = Laptop.objects.filter('price', 'id').first()
    return f"{laptop.brand} is the most expensive laptop available for  {laptop.price} $!"


def bulk_create_laptops(*args: List[Laptop]):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.filter(brand='Asus').update(operation_system='Windows')
    Laptop.objects.filter(brand='Apple').update(operation_system='MacOS')
    Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='linux')
    Laptop.objects.filter(brand='Lenovo').update(operation_system='Chrome OS')


def delete_inexpencive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


# Create three instances of Laptop
def bulk_create_chess_players(*args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title__in='no title').delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title__in='GM').update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title__in='no title').update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=(2399, 2300)).update(title='IM')


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=(2299, 2200)).update(title='FM')


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=(2199, 0)).update(title='regular player')

def set_new_chefs() -> None:
    Meal.objects.filter(meal_type__exact='Breakfast').update(chef='Gordon Ramsay')
    Meal.objects.filter(meal_type__exact='Lunch').update(chef='Julia Child')
    Meal.objects.filter(meal_type__exact='Dinner').update(chef='Jamie Oliver')
    Meal.objects.filter(meal_type__exact='Snack').update(chef='Thomas Keller')

def set_new_preparation_times() -> None:
    Meal.objects.filter(meal_type__exact='Breakfast').update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type__exact='Lunch').update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type__exact='Dinner').update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type__exact='Snack').update(preparation_time='5 minutes')

def update_low_calorie_meals() ->None:
    Meal.objects.filter(meal_type__in=['Breakfast', 'Diner']).update(calories=400)

def update_high_calorie_meals()-> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)

def delete_lunch_and_snack_meals()-> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()








