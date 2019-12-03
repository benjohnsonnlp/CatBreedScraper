import json

import requests
from bs4 import BeautifulSoup

from app.model import db, Kitty, User

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

    db.session.add(Kitty(
        name=breed_name,
        country=country,
        origin=origin,
        body=body,
        coat=coat,
        pattern=pattern,
        image_url=image_url,
    ))
db.session.add(User(username="Ben", email="ben.johnson@umbc.edu"))
db.session.commit()

# print(breeds)
