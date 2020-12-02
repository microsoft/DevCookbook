import os


def write_home_page(home_page: str):
    """Writes the home_page HTML to file

    Args:
        home_page (str): A string of HTML to be written to file
    """

    with open("./docs/index.html", "w+") as f:
        f.write(home_page)


def write_page(slug: str, page: str):
    """Writes the page HTML to `/{slug}/index.html`

    Args:
        slug (str):
        page (str): A string of HTML to be written to file
    """

    assert slug != "index"

    if not os.path.exists(f"./docs/{slug}"):
        os.makedirs(f"./docs/{slug}")

    with open(f"./docs/{slug}/index.html", "w+") as f:
        f.write(page)
