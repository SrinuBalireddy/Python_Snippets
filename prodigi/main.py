import PIL.Image
import markdown
from fastapi import FastAPI
from pydantic import BaseModel
from io import BytesIO
import requests


app = FastAPI()


# BaseModel for Image URL
class Image(BaseModel):
    image_url: str


# Colors Inventory
inventory = [
    {"key": "black", "red": 36, "green": 36, "blue": 36},
    {"key": "navy", "red": 0, "green": 0, "blue": 80},
    {"key": "teal", "red": 0, "green": 98, "blue": 110},
    {"key": "grey", "red": 56, "green": 70, "blue": 87}
]


def fetch_rgb(image_url):
    """
    fetches the payload data from the image url and returns rgb values of the image
    :param image_url: str
    :return: rgb values
    """
    data = dict(image_url)
    img_request = requests.get(data['image_url'])
    img = PIL.Image.open(BytesIO(img_request.content))
    return img.getpixel((320, 240))


def search_color(rgb_values):
    """
    compares the Payload image rgb values with the inventory
    and returns Matching color is exists in inventory else
    returns the string 'No Matching color'
    :param rgb_values:
    :return: Matching color/ No matching color
    """
    for color_dict in inventory:
        if color_dict['red'] == rgb_values[0] and color_dict['green'] == rgb_values[1] \
                and color_dict['blue'] == rgb_values[2]:
            return color_dict['key']
    return 'No matching color'  # future enhancement - update the inventory with new rgb and color key
    # if the No matching color is found


@app.get('/')
def index():

    # open the read me file
    with open('README.md', 'r') as markdown_file:

        # read the contents of the file
        content = markdown_file.read()

        # convert to HTML file
        return markdown.markdown(content)


@app.post('/image')
def get_color(image_url: Image):
    try:
        rgb_values = fetch_rgb(image_url)
    except PIL.UnidentifiedImageError:
        return 'Invalid image url'
    return search_color(rgb_values)