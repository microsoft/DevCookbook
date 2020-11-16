from recipe_compiler.parsing import parse_content, render_recipe_name


def test_render_recipe_name():
    # Given
    recipe_name = "Recipe name"

    source = f"""# {recipe_name}

> [Quote]

## Ingredients

## Instructions

"""

    # When
    actual_recipe_name = render_recipe_name(parse_content(source))

    # Then
    assert recipe_name == actual_recipe_name


def test_render_quote():
    # Given
    quote = "This is the quote I am looking for."

    source = f"""# Recipe name

> {quote}

## Ingredients

## Instructions

"""

    # When
    actual_quote = render_recipe_name(parse_content(source))

    # Then
    assert quote == actual_quote