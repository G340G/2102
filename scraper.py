import wikipedia
import requests
import random

def get_keyword():
    base = random.choice(open("generator/keyword_pool.txt").read().splitlines())
    suffix = str(random.randint(1000,999999))
    return f"{base}_{suffix}"

def scrape_text(keyword):
    try:
        page = wikipedia.page(keyword, auto_suggest=True)
        return page.content[:2000]
    except:
        return "Signal corrupted."

def scrape_image(keyword):
    url = f"https://picsum.photos/seed/{keyword}/640/480"
    img = requests.get(url).content
    with open("generator/temp.jpg","wb") as f:
        f.write(img)
