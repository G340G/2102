import wikipedia
import requests
import random
from PIL import Image
from io import BytesIO

def scrape_text(keyword):
    try:
        page = wikipedia.page(keyword.split("_")[0])
        return page.content[:2000]
    except:
        return "Transmission unstable. Data incomplete."

def scrape_image(keyword):
    try:
        url = f"https://picsum.photos/seed/{keyword}/640/480"
        r = requests.get(url, timeout=10)
        img = Image.open(BytesIO(r.content))
        img.save("frame.jpg")
    except:
        Image.new("RGB",(640,480),(0,0,0)).save("frame.jpg")
