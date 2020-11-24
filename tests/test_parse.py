from recipe_compiler.parse import (
    get_ingredients,
    get_instructions,
    get_quote,
    get_recipe_name,
)

import marko

SOURCE_TEXT = f"""# Recipe name

> This is a test quote
> for which this is the second line

## Ingredients

- Ingredient 1
- Ingredient 2

## Directions

1. Instruction 1
2. Instruction 2

"""


def test_get_recipe_name():
    # Given
    expected = "Recipe name"

    source = marko.parse(SOURCE_TEXT)

    # When
    actual = get_recipe_name(source)

    # Then
    assert expected == actual


def test_get_quote():
    # Given
    expected = "This is a test quote\nfor which this is the second line"

    source = marko.parse(SOURCE_TEXT)

    # When
    actual = get_quote(source)

    # Then
    assert expected == actual


def test_get_ingredients():
    # Given
    expected = ["Ingredient 1", "Ingredient 2"]

    source = marko.parse(SOURCE_TEXT)

    # When
    actual = get_ingredients(source)

    # Then
    assert expected == actual


def test_get_instructions():
    # Given
    expected = ["Instruction 1", "Instruction 2"]

    source = marko.parse(SOURCE_TEXT)

    # When
    actual = get_instructions(source)

    # Then
    assert expected == actual
