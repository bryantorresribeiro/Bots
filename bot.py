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

contatos = ["lele", "dani", "buja", "bessa", "ale", "jão", "6 anões e 1 gigante FDRAL"]

def gerador_de_frase():
    apiRequest = requests.get('https://api.chucknorris.io/jokes/random')
    requestJson = apiRequest.json()
    return requestJson['value']

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

time.sleep(5)

true = 0
while true == 0:
    for contato in contatos:
        time.sleep(1)
        buscar_contato(contato)
        mensagem = gerador_de_frase()     
        enviar_mensagem(mensagem)

    
    
