"""CP1404 Prac 10 - Wikipedia API & Python Library"""

import wikipedia
from bs4 import GuessedAtParserWarning
import warnings

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

title = input("Enter page title: ")
while title != "":
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(page.summary.strip())
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError as e:
        print(f"Page id: {title} does not match any pages. Try another id!")
    print()
    title = input("Enter page title: ")
print("Thank you.")
