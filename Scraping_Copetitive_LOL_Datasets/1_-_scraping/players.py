from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from time import sleep

username = 'username'
password = 'senha'


path = './1_-_scraping/chromedriver.exe'
url_to_login = "http://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT03/1102245?gameHash=09a8c951db73b32e"
df = pd.read_csv('./1_-_scraping/links_to_scraping.csv')
df2 = pd.read_csv('./2_-_html_filtering/web_pages_html.csv')


urls = df[df.columns[1]]

#urls de teste:
#urls = ['http://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT03/1102245?gameHash=09a8c951db73b32e','https://matchhistory.br.leagueoflegends.com/pt/#match-details/ESPORTSTMNT03/530278?gameHash=9a50b413596795c1','https://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT01/1370145?gameHash=43cb3a4747f70599']


driver = webdriver.Chrome(executable_path=path)
driver.get(url_to_login)
sleep(5)
driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input""").send_keys(username)
driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input""").send_keys(password)
driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/button""").click()
sleep(8)

#list_names = []
html_names = []
delay = 2
c = 0
for url in urls:
    c+=1
    driver.get(url)
    sleep(delay)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    names = soup.find_all('div', {'class':'champion-nameplate-name'})
    for i in range(0,len(names)):
        names[i] = str(names[i])
    names = ';;;;;'.join(names)
    html_names.append(names)
    print(c)
df2['names'] = html_names
df2.to_csv('test.csv')
driver.quit()
