import requests
from bs4 import BeautifulSoup
import time
from rich.console import Console
import json


console = Console()

def save_recipe_file(file_name, recipe, link):
    try:
        with open(file_name, 'a') as file:
            file.write(f'recipe: {recipe}\n')
            file.write(f'link: {link}\n')
    except Exception as e:
        print(f'An error has occurred: {e}')

def get_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print('Error. Request timed out.')
    except requests.exceptions.RequestException as err:
        print(f'Erro: {err}')
    return None

def add_recipe(recipes, title, url):
    recipes.append(
        {'recipe': title, 'url': url}
    )

def get_recipes(req, recipes):
    soup = BeautifulSoup(req.text, 'lxml')

    main = soup.select('.post.type-post')

    for item in main:
        title = item.select_one('.entry-title-link').text
        url = item.select_one('.entry-title-link')['href']
        add_recipe(recipes, title, url)

def welcome_message():
    console.print("=" * 60, style="bold blue")
    console.print("🌐 [bold green]Web Scraping in Progress...[/]")
    console.print("=" * 60, style="bold blue")
    console.print("\n🚀 [bold cyan]Starting the scraping process...[/]\n")
    console.print("🔍 [bold yellow]Scraping URLs:[/]\n")

def scraping_url_message(url, status):
    console.print(f"   - 🕵️‍♂️ [bold green]Target:[/] {url}{status}")

def create_recipe_json(recipes):
    with open('all_recipes.json', 'w', encoding='utf-8') as file:
        json.dump(recipes, file, indent=4, ensure_ascii=False) # indent=4 for pretty formatting
    console.print("\n" + "=" * 60, style="bold blue")
    console.print("✅ [bold green]Saved recipes to `all_recipes.json`📜")
    console.print("=" * 60, style="bold blue")

def end_scrape_message():
    console.print("\n" + "=" * 60, style="bold blue")
    console.print("✅ [bold green]Scraping complete![/] 🥳")
    console.print("=" * 60, style="bold blue")


def main():
    recipes= []

    pages = 224
    i = 1

    welcome_message()
    
    while i <= pages:
        url = f'https://panlasangpinoy.com/recipes/page/{i}'

        req = get_request(url)

        if req:
            status = '[200]OK'

            scraping_url_message(url, status)
            get_recipes(req, recipes)
        else:
            print('Failed to retrieve page')
        i += 1

        # 1 second delay per request
        time.sleep(1)

    # Create json file for all recipes
    create_recipe_json(recipes)
    
    # End message
    end_scrape_message()

main()
