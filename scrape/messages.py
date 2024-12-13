from rich.console import Console

# Initialize console for rich output
console = Console()

def welcome_message() -> None:
    """
    Prints a welcome message indicating the scraping process is starting.

    Returns:
        None
    """
    console.print("=" * 60, style="bold blue")
    console.print("🌐 [bold green]Web Scraping in Progress...[/]")
    console.print("=" * 60, style="bold blue")
    console.print("\n🚀 [bold cyan]Starting the scraping process...[/]\n")
    console.print("🔍 [bold yellow]Scraping URLs:[/]\n")


def scraping_url_message(url: str, status: str) -> None:
    """
    Prints the current URL being scraped with its status code.

    Args:
        url (str): The URL that is being scraped.
        status (str): The status of the request (e.g., '[200]OK').

    Returns:
        None
    """
    console.print(f"   🕵️‍♂️ [bold green]Target:[/] {url} {status}")


def end_scrape_message() -> None:
    """
    Prints a message indicating the scraping process is complete.

    Returns:
        None
    """
    console.print("\n" + "=" * 60, style="bold blue")
    console.print("✅ [bold green]Scraping complete![/] 🥳")
    console.print("=" * 60, style="bold blue")
