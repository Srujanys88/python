import requests
import bs4
from PIL import Image
num = input("Enter a number")

url = "https://xkcd.com/"+num

response = requests.get(url)
bs = bs4.BeautifulSoup(response.text, 'html.parser')
soupelement = bs.select("#comic img")
imageurl = "https://xkcd.com/"+soupelement[0].get('src')
imageresponse = requests.get(imageurl)
f = open('image.jpg','wb')
for chunks in imageresponse.iter_content(1):
    f.write(chunks)
f.close()

img = Image.open('image.jpg')
img.show()

