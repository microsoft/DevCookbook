from jinja2 import Environment, PackageLoader, select_autoescape

import sys

print(sys.path)

from recipe_compiler.read import read_recipe_file
from recipe_compiler.parse import parse_to_recipe
from recipe_compiler.render import render_home_page, render_recipe_page
from recipe_compiler.write import write_home_page, write_recipe_page

import glob
import os

if __name__ == "__main__":
    # Read
    recipe_files = glob.glob("../recipes/*.md")
    recipe_contents = [read_recipe_file(recipe_file) for recipe_file in recipe_files]

    # Parse
    recipes = [parse_to_recipe(recipe_content) for recipe_content in recipe_contents]

    # Render
    env = Environment(
        loader=PackageLoader("recipe_compiler", "templates"),
        autoescape=select_autoescape(["html"]),
    )
    home_page = render_home_page(recipes, env)
    recipe_pages = zip(
        [recipe.slug for recipe in recipes],
        [render_recipe_page(recipe, env) for recipe in recipes],
    )

    # Write
    write_home_page(home_page)
    for recipe_slug, recipe_page in recipe_pages:
        write_recipe_page(recipe_slug, recipe_page)
