import pyshorteners
import validators
import pyperclip
import requests
from colorama import Fore, Style, init

class URLShortener:
    """
    QuickLink: Advanced URL Shortener
    A class to shorten URLs using different services.
    This class encapsulates the shortening functionality and supports multiple services.
    """
    def __init__(self, bitly_api_key):
        """Initialize the URLShortener with a shortener object and a service mapping."""
        self.shortener = pyshorteners.Shortener(api_key=bitly_api_key)
        self.service_mapping = {
            "tinyurl": self.shortener.tinyurl.short,
            "bitly": self.shortener.bitly.short,
            "isgd": self.shortener.isgd.short
        }

    def shorten_url(self, url, service="TinyURL"):
        """
        Shorten a URL using the specified shortening service.
        
        Args:
            url (str): The URL to be shortened.
            service (str): The shortening service to use (default is TinyURL).

        Returns:
            str: The shortened URL.

        Raises:
            ValueError: If the URL is invalid or the service is not supported.
            ConnectionError: If there is no Internet connection.
        """
        if not validators.url(url):
            raise ValueError("The URL entered is not valid.")
        
        if not self.check_internet_connection():
            raise ConnectionError("No Internet connection. Please check your connection.")

        try:
            short_function = self.service_mapping[service.lower()]
        except KeyError:
            raise ValueError("The shortening service is not valid.")
        
        return short_function(url)

    def check_internet_connection(self):
        """Check if there is an Internet connection by pinging Google."""
        try:
            requests.get("https://www.iqdotnet.net", timeout=5)
            return True
        except requests.ConnectionError:
            return False

def main():
    """Main function to run the QuickLink: Advanced URL Shortener in a loop until the user decides to exit."""
    init(autoreset=True)  # Initialize colorama to automatically reset colors
    print(Fore.CYAN + "Welcome to QuickLink: Advanced URL Shortener")
    
    # Definir la clave de API de Bitly
    bitly_api_key = 'YOUR_BITLY_API_KEY'
    
    url_shortener = URLShortener(bitly_api_key)

    try:
        while True:
            url = input("Enter the URL to shorten (or 'exit' to exit): ")
            if url.lower() == "exit":
                print(Fore.GREEN + "Goodbye!")
                break

            service = input("Choose the URL shortening service (TinyURL, Bitly, IS.gd): ")
            
            try:
                shortened_url = url_shortener.shorten_url(url, service)
                print(Fore.YELLOW + "Shortened URL: " + Fore.LIGHTGREEN_EX + shortened_url)
                pyperclip.copy(shortened_url)
                print(Fore.GREEN + "Shortened URL copied to clipboard.")
            except ValueError as e:
                print(Fore.RED + "Error: " + str(e))
            except ConnectionError as e:
                print(Fore.RED + "Error: " + str(e))
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProgram interrupted. Goodbye!")

if __name__ == "__main__":
    main()
