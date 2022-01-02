import requests
from bs4 import BeautifulSoup

i = 1
url = "https://www.goodreads.com/work/quotes/835372-cuentos-completos" + f"?page={i}"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

raw_quote = soup.find_all("div", class_= "quoteText")
raw_author = soup.find("a", class_ = "authorName")

author = str(raw_author.get_text(strip=True))

print(author + "\n")
for i in raw_quote:
    quote_text = str((i.get_text(strip=True)))
    quote = quote_text[:quote_text.rindex('”')+1]

    print(quote+ "\n")
    
        




#quote_string = (str(quote.get_text(strip=True)))

#print(quote_string)




