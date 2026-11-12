import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/", timeout=10)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

for book in soup.select("article.product_pod"):
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").get_text(strip=True)
    print(title, price)