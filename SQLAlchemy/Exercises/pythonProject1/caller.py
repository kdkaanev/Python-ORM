from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from mod import Recipe

DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy_ex'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions
    )
    session.add(new_recipe)


@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str):
    session.query(Recipe).filter_by(name=name).update(
        {
            Recipe.name: new_name,
            Recipe.ingredients: new_ingredients,
            Recipe.instructions: new_instructions,
        }
    )
@session_decorator(session)
def delete_recipe_by_name(name: str):
    session.query(Recipe).filter_by(name=name).delete()

@session_decorator(session)
def get_recipes_by_ingredient(ingredient_name: str):
    return session.query(Recipe).filter(Recipe.ingredients.ilike(f"%{ingredient_name}%"))


ingredient_to_filter = 'Chicken'
filtered_recipes = get_recipes_by_ingredient('Chicken')
print(filtered_recipes)
print(f"Recipes containing {ingredient_to_filter}:")
for recipe in filtered_recipes:
    print(f"Recipe name - {recipe.name}")


