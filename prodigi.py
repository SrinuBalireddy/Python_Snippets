# Write your code here :-)
from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image as Image
from io import BytesIO
import requests

app = FastAPI()

class Image(BaseModel):
    image_url: str

"""
@app.get('/')
def index():
    return {'key':'value'}
"""

@app.post('/image')
def get_color(image_url: Image):
    data = dict(image_url)
    imgRequest = requests.get(data['image_url'])
    img = Image.open(BytesIO(imgRequest.content))
    colors = img.getpixel((320, 240))
    return colors
    # return imgRequest.text[:20]
