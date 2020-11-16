import marko
from marko.block import Document


def read_recipe_file(filename: str) -> str:
    """Reads and returns text from the given file

    Args:
        filename (str): The file to be read

    Returns:
        str: The text of the given file
    """

    with open(filename, "r") as file:
        return file.read()


def parse_content(content: str) -> Document:
    return marko.parse(content)


def render_recipe_name(document: Document) -> str:
    for node in document.children:
        if node.level == 1:
            return node.children[0].children


def parse_recipe_ingredients(document: Document) -> str:
    for node in document.children:
        print(node)
    return ""