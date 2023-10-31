import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon

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


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=['Breakfast', 'Diner']).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


def show_hard_dungeons() -> str:
    dungeons = Dungeon.objects.filter(difficulty__exact='Hard').order_by('-location')
    result = [
        f"{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!"
        for d in dungeons
    ]
    return '\n'.join(result)


def bulk_create_dungeons(*args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names() -> None:
    Dungeon.objects.filter(difficulty__exact='Easy').update(name='The Erased Thombs')
    Dungeon.objects.filter(difficulty__exact='Medium').update(name='The Coral Labyrinth')
    Dungeon.objects.filter(difficulty__exact='Hard').update(name='The Lost Haunt')


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty__exact='Easy').update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.filter(difficulty__exact='Easy').update(recommended_level=25)
    Dungeon.objects.filter(difficulty__exact='Medium').update(recommended_level=50)
    Dungeon.objects.filter(difficulty__exact='Hard').update(recommended_level=75)


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


def set_new_locations() -> None:
    Dungeon.objects.filter(recommended_level=25).update(location='Enchanted Maze')
    Dungeon.objects.filter(recommended_level=50).update(location='Grimstone Mines')
    Dungeon.objects.filter(recommended_level=75).update(location='Shadowed Abyss')

# Create two instances
dungeon1 = Dungeon(
    name="Dungeon 1",
    boss_name="Boss 1",
    boss_health=1000,
    recommended_level=75,
    reward="Gold",
    location="Eternal Hell",
    difficulty="Hard",
)

dungeon2 = Dungeon(
    name="Dungeon 2",
    boss_name="Boss 2",
    boss_health=500,
    recommended_level=25,
    reward="Experience",
    location="Crystal Caverns",
    difficulty="Easy",
)

# Bulk save the instances
bulk_create_dungeons([dungeon1, dungeon2])

# Update boss's health
update_dungeon_bosses_health()

# Show hard dungeons
hard_dungeons_info = show_hard_dungeons()
print(hard_dungeons_info)

# Change dungeon names based on difficulty
update_dungeon_names()
dungeons = Dungeon.objects.all()
print(dungeons[0].name)
print(dungeons[1].name)

# Change the dungeon rewards
update_dungeon_rewards()
dungeons = Dungeon.objects.all()
print(dungeons[0].reward)
print(dungeons[1].reward)
