import re
import os
import requests

r = requests.get("https://en.wikipedia.org/wiki/List_of_India_ODI_cricketers")

f = open("list_of_cricketers.html", "wb")
f.write(r.text.encode())
f.close()

p = re.compile()

