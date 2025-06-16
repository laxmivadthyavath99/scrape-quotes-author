import requests
from bs4 import BeautifulSoup
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
        data.append({
            'Quote': text.text.strip(),
            'Author': author.text.strip()
        })
        print(f"{text.text.strip()} - {author.text.strip()}")

df = pd.DataFrame(data)  # ✅ Corrected this line
df.to_excel('quotes.xlsx', index=False)

if os.path.exists('quotes.xlsx'):
    print("File saved successfully!")
    df_check = pd.read_excel('quotes.xlsx')
    print(df_check.head())
else:
    print("File not found. Something went wrong.")
