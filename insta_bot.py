from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

def account_info():
    with open('info_account.txt', 'r') as f:
        info = f.read().split()
        username = info[0]
        password = info[1]
    return username, password

username, password = account_info()


options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get('https://www.instagram.com/')
username_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'


time.sleep(2)

driver.find_element_by_xpath(username_xpath).send_keys(username)
time.sleep(2)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(2)
pyautogui.hotkey('enter')