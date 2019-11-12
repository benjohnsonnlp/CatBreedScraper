import json

import requests
from bs4 import BeautifulSoup


cat_html = requests.get("https://en.wikipedia.org/wiki/List_of_cat_breeds").text

soup = BeautifulSoup(cat_html, "html.parser")

heading = soup.select("#firstHeading")[0].text

rows = soup.select("table.wikitable tr")[1:]

breeds = {}

for row in rows:
    breed_name = row.select("th")[0].text.strip()
    td = row.select("td")

    country = td[0].text
    origin = td[1].text
    body = td[2].text.strip()
    coat = td[3].text
    pattern = td[4].text
    images = td[5].select("img")
    if images:
        image_url = images[0].attrs["src"]

    kitty = {
        "name": breed_name,
        "country": country,
        "origin": origin,
        "body": body,
        "coat": coat,
        "pattern": pattern,
        "imageUrl": image_url,
    }
    breeds[breed_name] = kitty

print(json.dumps(breeds, indent=4))

# print(breeds)
