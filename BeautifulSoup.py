import requests
from bs4 import BeautifulSoup
from datetime import datetime

import webbrowser

# print(datetime.date())
page = requests.get('https://www.bing.com/')
# Create a BeautifulSoup object
print(2)
soup = BeautifulSoup(page.text, 'html.parser')
print(3)
sp = str(soup)
print(4)
print(sp)
message = '''hey Sup,Welcome to the World of Programming.
Do you know we can make the inevitable happen using the techniques of prototyping.'''
print(message)
print(''' "Oh no", " "system is broken ''')

