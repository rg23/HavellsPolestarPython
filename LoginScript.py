from selenium import webdriver
from getpass import getpass
import time

from bs4 import BeautifulSoup
import requests
import urllib.request
import webbrowser

def captchaCodeBreaker(lin):
#    lin = "https://dashboard.havells.com/dwreports/"
#    link2 = "http://dashboarduat.havells.com/DW_reportsUAT"
#    webbrowser.open(lin)

    data = requests.get(lin).text
    # # print(data)
    soup = BeautifulSoup(data, "lxml")
    # print (soup)
    for link in soup.find_all('img', {'id': 'imgCaptcha'}):
        captcha = link.get('src')
    # print(captcha)
    best = (lin + captcha)
    f = open('captcha.jpg', 'wb')
    # print (best)

    f.write(urllib.request.urlopen(best).read())
    webbrowser.open(best)
    #print(best)
    # print(best)
    f.close()

def delay(t):
    time.sleep(t)
    return


if __name__ == '__main__':

    user = "edw.102@polestarllp.com"
    # input('Enter your username')

    pwd = "Havells@123"
    # getpass('Enter your password')

    captcha = "LKHA"

    lin = 'https://dashboard.havells.com/dwreports/'

    driver = webdriver.Chrome('C:\\Users\\User\\Desktop\\chromedriver_win32\\chromedriver.exe')
    driver.get('https://dashboard.havells.com/dwreports/')

    usr_box = driver.find_element_by_id('txtUnm')
    usr_box.send_keys(user)

    pwd_box = driver.find_element_by_id('txtPwd')
    pwd_box.send_keys(pwd)

    cptcha_box = driver.find_element_by_id('txtCaptcha')
    cptcha_box.send_keys(captcha)
    cpt = captchaCodeBreaker(lin)

    delay(2)
    login_button = driver.find_element_by_id('btnLogin')
    login_button.click()