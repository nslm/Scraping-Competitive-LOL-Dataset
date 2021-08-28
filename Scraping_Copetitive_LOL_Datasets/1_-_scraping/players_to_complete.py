from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from time import sleep

username = 'username'
password = 'passwaord'


path = './1_-_scraping/chromedriver.exe'
url_to_login = "http://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT03/1102245?gameHash=09a8c951db73b32e"
df = pd.read_csv('./test.csv')

#driver = webdriver.Chrome(executable_path=path)
#driver.get(url_to_login)
#sleep(5)
#driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input""").send_keys(username)
#driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input""").send_keys(password)
#driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/button""").click()
#sleep(8)


names = df['names']
lista_faltantes = []
for i in range(0,len(names)):
    if '<div class="champion-nameplate-name">' not in str(names[i]):
        lista_faltantes.append(i)
print(lista_faltantes)

#for faltantes in lista_faltantes:
    #url = df['url'][faltantes]
    #driver.get(url)
    #sleep(3)
    #html = driver.page_source
    #soup = bs(html, 'html.parser')
    #names = soup.find_all('div', {'class':'champion-nameplate-name'})
    #for i in range(0,len(names)):
        #names[i] = str(names[i])
    #names = ';;;;;'.join(names)
    #df['names'][faltantes] = names

#df.to_csv('test.csv')
#driver.quit()
