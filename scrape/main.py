import time
from rich.console import Console
from utils import get_request, get_recipes, save_recipe_file, create_recipe_json
from messages import welcome_message, scraping_url_message, end_scrape_message

console = Console()

def main() -> None:
    """
    Main function that orchestrates the scraping process.
    - Sends HTTP requests to the target website.
    - Parses the HTML to extract recipes.
    - Saves the extracted recipes to a JSON file.

    Returns:
        None
    """
    recipes: list[dict] = []  # List to store recipes

    pages = 224  # The number of pages to scrape
    i = 1  # Page counter

    welcome_message()  # Display welcome message
    
    while i <= 2:
        url = f'https://panlasangpinoy.com/recipes/page/{i}'

        req = get_request(url)

        if req:
            status = '[200]OK'  # Status for successful response
            scraping_url_message(url, status)
            get_recipes(req, recipes)
        else:
            print('Failed to retrieve page')
        
        i += 1  # Move to the next page
        time.sleep(1)  # 1 second delay to avoid hitting the server too fast

    # After scraping, save the recipes to a JSON file
    create_recipe_json(recipes)
    
    # Display completion message
    end_scrape_message()


if __name__ == "__main__":
    main()
