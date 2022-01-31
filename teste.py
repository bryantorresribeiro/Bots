from urllib import request
from selenium import webdriver
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os 

dir_path = os.getcwd()

profile = os.path.join(dir_path, "profile", "wpp")

options = webdriver.ChromeOptions()
options.add_argument(rf"user-data-dir={profile}")
options.add_argument('--log-level=3')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.get('https://web.whatsapp.com/')

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

time.sleep(5)

buscar_contato("lele")

post = driver.find_elements_by_class_name('selectable-text.copyable-text')
post[-2].text

print(post)