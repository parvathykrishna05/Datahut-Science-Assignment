from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def clean_price(x):
    if pd.isna(x):
        return None
    x = str(x)
    num = re.sub(r'\D', '', x)
    return float(num) if num else None

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

base_url = "https://www.myntra.com/women-dresses"
all_products = []
page = 1
products_seen = set()

while True:
    url = f"{base_url}?p={page}"
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    product_cards = soup.find_all("li", class_="product-base")
    if not product_cards:
        break

    for card in product_cards:
        brand = card.find("h3", class_="product-brand")
        prod_name = card.find("h4", class_="product-product")
        brand = brand.text.strip() if brand else None
        prod_name = prod_name.text.strip() if prod_name else None

        link_tag = card.find("a")
        product_url = "https://www.myntra.com" + link_tag["href"] if link_tag and link_tag.has_attr("href") else None

        if product_url in products_seen:
            continue
        products_seen.add(product_url)

        # Price extraction
        mrp_tag = card.find("span", class_="product-strike")
        price_tag = card.find("span", class_="product-discountedPrice")
        alt_price_tag = card.find("span", class_="product-price")
        mrp_text = mrp_tag.text if mrp_tag else alt_price_tag.text if alt_price_tag else None
        price_text = price_tag.text if price_tag else alt_price_tag.text if alt_price_tag else None
        mrp = clean_price(mrp_text)
        price = clean_price(price_text)

        # Ratings and reviews
        rating_val, reviews = None, None
        rating_block = card.find("div", class_="product-ratingsContainer")
        if rating_block:
            spans = rating_block.find_all("span")
            if spans:
                rating_val = spans[0].text.strip() if len(spans) > 0 else None
                reviews = spans[-1].text.strip("()") if len(spans) > 1 else None

        all_products.append({
            "Product Name": prod_name,
            "Brand": brand,
            "Category": "Women Dresses",
            "MRP": mrp,
            "Discounted Price": price,
            "Rating": rating_val,
            "Number of Reviews": reviews,
            "Product URL": product_url
        })
    print(f"Page {page}: Collected {len(all_products)} products so far...")
    if len(all_products) >= 350:
        break
    page += 1

driver.quit()

# Save to CSV
df = pd.DataFrame(all_products)
df.to_csv("myntra_womens_dresses_raw.csv", index=False, encoding="utf-8-sig")
print(f"\n✅ Raw scrape complete: {df.shape[0]} products saved to myntra_womens_dresses_raw.csv")
