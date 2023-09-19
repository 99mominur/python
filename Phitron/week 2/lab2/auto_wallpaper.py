import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(api_url)
content = response.content.decode("UTF-8")

# print(content)

dict_content = json.loads(content)

image_url = dict_content["url"]
# print(image_url)
# print(type(dict_content))


get_image = requests.get(image_url)

# print(get_image)

with open("apod.png", "wb") as image:
    image.write(get_image.content)
    image.close()

PyWallpaper.change_wallpaper("/home/mominur/myCode/python/Phitron/week 2/lab2/apod.png")