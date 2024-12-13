import requests
from bs4 import BeautifulSoup
import time
from rich.console import Console

data = []

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

def get_recipes(req):
    soup = BeautifulSoup(req.text, 'lxml')

    main = soup.select('.post.type-post')

    for item in main:
        title = item.select_one('.entry-title-link').text
        link = item.select_one('.entry-title-link')['href']
        save_recipe_file('all_recipes.txt', title, link)

def welcome_message():
    console.print("=" * 60, style="bold blue")
    console.print("🌐 [bold green]Web Scraping in Progress...[/]")
    console.print("=" * 60, style="bold blue")
    console.print("\n🚀 [bold cyan]Starting the scraping process...[/]\n")
    console.print("🔍 [bold yellow]Scraping URLs:[/]\n")

def scraping_url_message(url, status):
    console.print(f"   - 🕵️‍♂️ [bold green]Target:[/] {url}{status}")

def end_scrape_message():
    console.print("\n" + "=" * 60, style="bold blue")
    console.print("✅ [bold green]Scraping complete![/] 🥳")
    console.print("=" * 60, style="bold blue")


def main():
    pages = 224
    i = 1

    welcome_message()
    
    while i <= pages:
        url = f'https://panlasangpinoy.com/recipes/page/{i}'

        req = get_request(url)

        if req:
            status = '[200]OK'

            scraping_url_message(url, status)
            get_recipes(req)
        else:
            print('Failed to retrieve page')
        i += 1

        # 1 second delay per request
        time.sleep(1)


    end_scrape_message()

main()
