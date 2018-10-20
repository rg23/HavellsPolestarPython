from bs4 import BeautifulSoup
import requests
import urllib.request
import webbrowser

#lin = "https://dashboard.havells.com/dwreports/"
lin = "http://dashboarduat.havells.com/DW_reportsUAT/"
webbrowser.open(lin)

data = requests.get(lin).text
# # print(data)
soup = BeautifulSoup(data, "lxml")
# print (soup)
for link in soup.find_all('img',{'id':'imgCaptcha'}):
    captcha = link.get('src')
# print(captcha)
best = (lin+captcha)
f = open('captcha.jpg','wb')
# print (best)

f.write(urllib.request.urlopen(best).read())
webbrowser.open(best)
# print(best)
# print(best)
f.close()
