import requests
import os

page = requests.get('https://en.wikipedia.org/wiki/List_of_India_Test_cricketers')

f = open("list_of_cricketers.html", "wb")
f.write(page.text.encode())
f.close()

