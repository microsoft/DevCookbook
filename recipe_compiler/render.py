from jinja2 import Environment
from recipe_compiler.recipe import Recipe


def render_recipe_page(recipe: Recipe, env: Environment) -> str:
    """Formats an HTML page for a given Recipe, returned as a str

    Args:
        recipe (Recipe): The Recipe object to render
        env (Environment): A Jinja environment

    Returns:
        str: HTML representing the Recipe
    """

    return env.get_template("recipe.html").render(recipe=recipe)


def render_home_page(recipes: list[Recipe], env: Environment) -> str:
    """Formats an HTML page to serve as a hub for all recipes

    Args:
        recipes (list[Recipe]): A list of Recipe objects
        env (Environment): A Jinja environment

    Returns:
        str: HTML home page with links to all recipes
    """

    recipes_by_category = {}
    for recipe in recipes:
        if recipe.category in recipes_by_category.keys():
            recipes_by_category[recipe.category.value].append(recipe)
        else:
            recipes_by_category[recipe.category.value] = [recipe]

    return env.get_template("homepage.html").render(
        recipes_by_category=recipes_by_category
    )
