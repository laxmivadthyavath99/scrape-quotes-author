import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import os
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.select('div.quote')
data = []
for quote in quotes:
    text = quote.select_one('span.text')
    author = quote.select_one('small.author')
    if text and author:
        data.append({"Quote": text.text.strip(), "Author": author.text.strip()})
df = pd.DataFrame(data)
df.to_excel("scrape1.xlsx", index=False)
print("Data saved to scrape1.xlsx")
df.to_excel("scrape2.xlsx", index=False)
print("Data also saved to scrape2.xlsx")
print("Current working directory:", os.getcwd())
