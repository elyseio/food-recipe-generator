import requests
from bs4 import BeautifulSoup

data = []

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


def main():
    url = 'https://panlasangpinoy.com/recipes'
    
    req = get_request(url)
    if req:
        get_recipes(req)
    else:
        print('Failed to retrieve page')

main()
