import requests
from bs4 import BeautifulSoup

# Set initial value for the page number
i = 1

# Create the URL string with the page number appended
url = "" + f"?page={i}"

# Send an HTTP request to the URL and fetch the content
page = requests.get(url)

# Parse the content with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

# Extract the raw quote text and raw author name
raw_quote = soup.find_all("div", class_= "quoteText")
raw_author = soup.find("a", class_ = "authorName")

# Remove any whitespace and supplementary content from the author name
author = str(raw_author.get_text(strip=True))

# Print the author name
print(author + "\n")

# Iterate through the list of raw quotes
for i in raw_quote:
    # Remove any white space and supplementary content from the quote
    quote_text = str((i.get_text(strip=True)))
    
    # Extract the quote from the quote_text string
    quote = quote_text[:quote_text.rindex('”')+1]

    # Print the quote
    print(quote+ "\n")