import requests
from bs4 import BeautifulSoup
import json
from typing import Optional, List, Dict
from rich.console import Console

console = Console()

def get_request(url: str) -> Optional[requests.Response]:
    """
    Sends an HTTP GET request to the provided URL with error handling.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        Optional[requests.Response]: The response object if successful, None if failed.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response
    except requests.exceptions.Timeout:
        print('Error. Request timed out.')
    except requests.exceptions.RequestException as err:
        print(f'Error: {err}')
    return None


def add_recipe(recipes: List[Dict[str, str]], title: str, url: str) -> None:
    """
    Adds a recipe to the list of recipes.

    Args:
        recipes (List[Dict[str, str]]): The list to store recipe dictionaries.
        title (str): The title of the recipe.
        url (str): The URL of the recipe.

    Returns:
        None
    """
    recipes.append({'recipe': title, 'url': url})


def get_recipes(req: requests.Response, recipes: List[Dict[str, str]]) -> None:
    """
    Parses the HTML response to extract recipe titles and URLs, and adds them to the recipes list.

    Args:
        req (requests.Response): The HTTP response object containing the HTML content.
        recipes (List[Dict[str, str]]): The list to store parsed recipe data.

    Returns:
        None
    """
    soup = BeautifulSoup(req.text, 'lxml')
    main = soup.select('.post.type-post')  # Adjust selector to your website's structure

    for item in main:
        title = item.select_one('.entry-title-link').text
        url = item.select_one('.entry-title-link')['href']
        add_recipe(recipes, title, url)


def create_recipe_json(recipes: List[Dict[str, str]]) -> None:
    """
    Saves the list of recipes to a JSON file.

    Args:
        recipes (List[Dict[str, str]]): The list of recipes to be saved.

    Returns:
        None
    """
    with open('../data/all_recipes.json', 'w', encoding='utf-8') as file:
        json.dump(recipes, file, indent=4, ensure_ascii=False)
    console.print("\n✅ [bold green]Saved recipes to `all_recipes.json`📜")


def save_recipe_file(file_name: str, recipe: str, link: str) -> None:
    """
    Appends a recipe's title and URL to a text file.

    Args:
        file_name (str): The file where the recipe should be saved.
        recipe (str): The recipe's title.
        link (str): The recipe's URL.

    Returns:
        None
    """
    try:
        with open(file_name, 'a') as file:
            file.write(f'recipe: {recipe}\n')
            file.write(f'link: {link}\n')
    except Exception as e:
        print(f'An error has occurred: {e}')
