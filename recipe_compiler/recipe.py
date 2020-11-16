from dataclasses import dataclass
from .recipe_category import RecipeCategory
import frontmatter


@dataclass
class Recipe:
    name: str
    residence: str
    category: RecipeCategory
    recipe_name: str
    quote: str
    ingredients: str
    instructions: str

    @staticmethod
    def from_recipe_text(recipe_text: str) -> "Recipe":
        recipe_data = frontmatter.loads(recipe_text)

        return Recipe(
            name=recipe_data["name"],
            residence=recipe_data["residence"],
            category=RecipeCategory(recipe_data["category"].lower()),
            recipe_name="",
            quote="",
            ingredients="",
            instructions="",
        )
