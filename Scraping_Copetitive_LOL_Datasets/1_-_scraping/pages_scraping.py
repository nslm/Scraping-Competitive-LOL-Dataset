from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from time import sleep

username = 'username'
password = 'password'


path = './1_-_scraping/chromedriver.exe'
url_to_login = "http://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT03/1102245?gameHash=09a8c951db73b32e"
df = pd.read_csv('./1_-_scraping/links_to_scraping.csv')

urls = df[df.columns[1]]

#urls de teste:
urls = ['http://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT03/1102245?gameHash=09a8c951db73b32e','https://matchhistory.br.leagueoflegends.com/pt/#match-details/ESPORTSTMNT03/530278?gameHash=9a50b413596795c1','https://matchhistory.na.leagueoflegends.com/en/#match-details/ESPORTSTMNT01/1370145?gameHash=43cb3a4747f70599']


driver = webdriver.Chrome(executable_path=path)
driver.get(url_to_login)
sleep(5)
driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/input""").send_keys(username)
driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/input""").send_keys(password)
driver.find_element_by_xpath("""/html/body/div/div/div/div[2]/div/div/button""").click()
sleep(8)

tempos_dos_jogos = []
datas = []
resultados_blue = []
resultados_red = []
golds_blue = []
golds_red = []
kills_blue = []
kills_red = []
sumarios_inf_blue = []
sumarios_inf_red = []
tempos_dos_frist_bloods = []
tempos_das_frist_towers = []
html_names = []
tables = []
valores_maximos_dos_graficos = []
valores_dos_graficos = []
valores_dos_mapas = []

i = 0
for link in urls:
    delay = 2
    url = link
    if '&tab=overview' in link:
        url = link[0:-13]
    driver.get(url)
    sleep(delay)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    table = None
    tempo_do_jogo = None
    data = None
    resultado_red = None
    gold_blue = None
    gold_red = None
    kill_blue = None
    kill_red = None
    tempo_frist_blood = None
    tempo_frist_tower = None
    valor_max_do_grafico = None
    valores_do_grafico = None
    valores_do_mapa = None
    html_names = None
    i+=1
    delay = 1
    while True:
        try:
            sumario_mapa = soup.find('div',{'class':'map-header-additional-details'}).find_all('div',{'class':'binding'})           
            tempo_do_jogo = sumario_mapa[1].contents[0]
            data = sumario_mapa[2].contents[0]
            sumarios = soup.find_all('div', {'class':'gs-container team-summary'})
            sumario_blue = sumarios[0]
            sumario_red = sumarios[1]
            resultado_blue = sumario_blue.find('div',{'class':'game-conclusion'}).contents[0]
            resultado_red = sumario_red.find('div',{'class':'game-conclusion'}).contents[0]
            gold_blue = sumario_blue.find('div',{'class':'gold'}).contents[0]
            gold_red = sumario_red.find('div',{'class':'gold'}).contents[0]
            kill_blue = sumario_blue.find('div',{'class':'kills'}).contents[0]
            kill_red = sumario_red.find('div',{'class':'kills'}).contents[0]
            sumario_inf = soup.find_all('div', {'class':'gs-container gs-half-gutter'})
            sumario_inf_blue = sumario_inf[0]
            sumario_inf_red = sumario_inf[1]
            names = soup.find_all('div', {'class':'champion-nameplate-name'})
            for i in range(0,len(names)):
                names[i] = str(names[i])
            names = ';;;;;'.join(names)
            html_names.append(names)
            table = soup.find('table').encode("utf-8")
            break

        except:
            delay += 1
            print('erro1')
            driver.get(url)
            sleep(delay)
            html = driver.page_source
            soup = bs(html, 'html.parser')
            if delay>5:
                print(url)
                print('full None')
                break
    delay = 1  
    while True:
        try:
            tempo_frist_blood = soup.find_all('div', {'class':'card-name'})[0].contents[0]
            tempo_frist_tower = soup.find_all('div', {'class':'card-name'})[1].contents[0]
            valor_max_do_grafico = soup.find_all('g', {'class':'tick'})[-1].find('text').contents[0]
            valores_do_grafico = soup.find_all('circle', {'class':'point champion-gold-8 team-200 player-3'})
            valores_do_mapa = soup.find_all('div', {'class':'event-map'})
            print(i)
            break
         
        except:
            delay += 1
            print('erro2')
            driver.get(url)
            sleep(delay)
            html = driver.page_source
            soup = bs(html, 'html.parser')
            if delay>5:
                print('pagina defeituosa')
                print(i)
                break

    tempos_dos_jogos.append(tempo_do_jogo)
    datas.append(data)
    resultados_blue.append(resultado_blue)
    resultados_red.append(resultado_red)
    golds_blue.append(gold_blue)
    golds_red.append(gold_red)
    kills_blue.append(kill_blue)
    kills_red.append(kill_red)
    sumarios_inf_blue.append(sumario_inf_blue)
    sumarios_inf_red.append(sumario_inf_red)
    tempos_dos_frist_bloods.append(tempo_frist_blood)
    tempos_das_frist_towers.append(tempo_frist_tower)
    tables.append(table)
    valores_maximos_dos_graficos.append(valor_max_do_grafico)
    valores_dos_graficos.append(valores_do_grafico)
    valores_dos_mapas.append(valores_do_mapa)

columns_names = ['url', 'tempo_do_jogo', 'data', 'resultado_blue', 'resultado_red', 'gold_blue', 'gold_red', 'kills_blue', 'kills_red', 'frist_bloods', 'frist_towers', 'sumario_inf_blue', 'sumarios_inf_red', 'valor_max_do_grafico', 'names', 'tables', 'html_do_grafico', 'html_do_mapa']

dataframe = pd.DataFrame(zip(urls, tempos_dos_jogos, datas, resultados_blue, resultados_red, golds_blue, golds_red, kills_blue, kills_red, tempos_dos_frist_bloods, tempos_das_frist_towers, sumarios_inf_blue, sumarios_inf_red, valores_maximos_dos_graficos, html_names, tables, valores_dos_graficos, valores_dos_mapas), columns=columns_names)
dataframe.to_csv('web_pages_htmt.csv')

driver.quit()



