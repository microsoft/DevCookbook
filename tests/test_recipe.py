from recipe_compiler.recipe import Recipe
from recipe_compiler.recipe_category import RecipeCategory


def test_from_recipe_text():
    # Given
    name = "First Last"
    residence = "City, State, Country"
    category = "dessert"
    recipe_name = "Recipe Name"
    quote = "Open source is great!"
    ingredients = "Ingredients"
    instructions = "Instructions"

    recipe_text = f"""---
name: {name}
residence: {residence}
category: {category}
---

# {recipe_name}

> {quote}

## Ingredients
{ingredients}
## Instructions
{instructions}
"""

    expected_category = RecipeCategory.DESSERT

    # When
    recipe = Recipe.from_recipe_text(recipe_text)

    # Then
    assert name == recipe.name
    assert residence == recipe.residence
    assert expected_category == recipe.category
    assert recipe_name == recipe.recipe_name
    assert quote == quote
    assert ingredients == ingredients
    assert instructions == instructions