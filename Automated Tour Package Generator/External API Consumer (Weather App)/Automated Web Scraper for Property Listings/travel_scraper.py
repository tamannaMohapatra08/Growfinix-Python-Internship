import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

for author in soup.find_all("small", class_="author"):
    authors.append(author.text)

data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

data.to_csv("scraped_data.csv", index=False)

print("Data scraped successfully!")
print(data.head())