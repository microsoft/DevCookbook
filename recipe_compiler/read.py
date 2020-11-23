def read_recipe_file(filename: str) -> str:
    """Reads and returns text from the given file

    Args:
        filename (str): The file to be read

    Returns:
        str: The text of the given file
    """

    with open(filename, "r") as file:
        return file.read()
