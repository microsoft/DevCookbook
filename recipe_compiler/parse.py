from marko.block import Document
from recipe_compiler.recipe import Recipe
from recipe_compiler.recipe_category import RecipeCategory

import marko
import frontmatter


def get_recipe_name(document: Document) -> str:
    """Returns the content of the first h1 (#) tag in a markdown document

    Args:
        document (Document): A Marko Markdown Document object

    Returns:
        str: The content of the first h1 tag in the document
    """

    for node in document.children:
        if node.level == 1:
            return node.children[0].children


def get_quote(document: Document) -> str:
    """Returns the content of the first quote (>) tag in a markdown document

    Args:
        document (Document): A Marko Markdown Document object

    Returns:
        str: The content of the first quote tag in the document
    """

    return ""


def get_ingredients(document: Document) -> list[str]:
    return [""]


def get_instructions(document: Document) -> list[str]:
    return [""]


def parse_to_recipe(content: str) -> Recipe:
    """Parse a Markdown formatted string to a Recipe object

    Args:
        content (str): A Markdown formatted string

    Returns:
        Recipe: A Recipe object representing the given content
    """

    recipe_metadata = frontmatter.loads(content)

    document = marko.parse(content)
    recipe_name = get_recipe_name(document)
    quote = get_quote(document)
    ingredients = get_ingredients(document)
    instructions = get_instructions(document)

    return Recipe(
        name=recipe_metadata["name"],
        residence=recipe_metadata["residence"],
        category=RecipeCategory(recipe_metadata["category"].lower()),
        recipe_name=recipe_name,
        quote=quote,
        ingredients=ingredients,
        instructions=instructions,
    )
