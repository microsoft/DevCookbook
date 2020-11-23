from recipe_compiler.recipe import Recipe
from recipe_compiler.recipe_category import RecipeCategory


def test_recipe_slug():
    # Given
    name = "Thomas Eckert"
    residence = "Seattle, WA"
    category = RecipeCategory("dessert")
    recipe_name = "Pie Shell Script"
    quote = "Hello, World"
    ingredients = [""]
    instructions = [""]

    expected = "pie-shell-script"

    # When
    recipe = Recipe(
        name, residence, category, recipe_name, quote, ingredients, instructions
    )

    # Then
    assert expected == recipe.slug
