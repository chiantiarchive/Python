import csv
import time
import requests

from bs4 import BeautifulSoup

PAGES = [
    'https://books.toscrape.com/',
    'https://books.toscrape.com/catalogue/page-2.html',
    'https://books.toscrape.com/catalogue/page-3.html',
]
RATINGS = {"One": 1,"Two": 2, "Three": 3, "Four": 4, "Five": 5}

rows = []
for url in PAGES:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.select("article.product_pod"):
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one("p.price_color")
        rating_tag = book.select_one("p.star-rating")
        if not (title_tag and price_tag and rating_tag):
            continue

        price = float(price_tag.get_text(strip=True).replace("\u00a3", ""))
        rating_word = rating_tag["class"][1]
        rows.append({
            'title': title_tag['title'],
            'price': price,
            'rating': RATINGS.get(rating_word, 0),
        })
    print(f"Scraped {url}: {len(rows)} books so far")
    time.sleep

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} books to books.csv")