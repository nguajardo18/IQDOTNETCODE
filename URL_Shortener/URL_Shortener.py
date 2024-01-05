import pyshorteners
import validators

def shorten_url(long_url, service='tinyurl'):
    try:
        if not validators.url(long_url):
            raise ValueError("Invalid URL. Please enter a valid URL.")

        shortener = pyshorteners.Shortener()
        
        if service == 'tinyurl':
            return shortener.tinyurl.short(long_url)
        
        # You can add more services here if desired.

    except Exception as e:
        return f"Error shortening URL: {e}"

def main():
    while True:
        long_url = input("Enter the URL to shorten: ")
        short_url = shorten_url(long_url)

        if short_url:
            print("Shortened URL: ", short_url)
        else:
            print("Failed to shorten URL.")

        another = input("Do you want to shorten another URL? (yes/no): ").lower()
        if another not in ['yes', 'y']:
            break

if __name__ == "__main__":
    main()
    
    #IQDOTNET CODE - By Nelson Guajardo
