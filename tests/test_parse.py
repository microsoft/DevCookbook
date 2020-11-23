from recipe_compiler.parse import get_recipe_name

import marko


def test_get_recipe_name():
    # Given
    recipe_name = "Recipe name"

    source = marko.parse(
        f"""# {recipe_name}

> [Quote]

## Ingredients

## Instructions

"""
    )

    # When
    actual_recipe_name = get_recipe_name(source)

    # Then
    assert recipe_name == actual_recipe_name
