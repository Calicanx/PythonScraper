import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.iana.org/help/example-domains'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text content
    text = soup.get_text()

    # Save the extracted text to a file
    with open('scraped_data.txt', 'w') as f:
        f.write(text)

    print("Data saved to scraped_data.txt")
else:
    print("Failed to fetch the website.")
