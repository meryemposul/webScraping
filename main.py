import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.pttavm.com/arama/bebek-oyuncak'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

names = s.find_all(class_='product-list-box-container-info-name')
prices = s.find_all(class_='price-box-price text-sm md:text-xl font-bold text-eGrey-900 h-4 md:h-auto')

product_list = []

if names and prices:
    for name, price in zip(names, prices):
        product = {
            "Ürün Adı": name.text.strip(),
            "Fiyatı": price.text.strip(),
        }
        product_list.append(product)

    with open('products.json', 'w', encoding='utf-8') as json_file:
        json.dump(product_list, json_file, ensure_ascii=False, indent=4)

    print("Veriler JSON dosyasına kaydedildi.")
else:
    print("Element not found.")
