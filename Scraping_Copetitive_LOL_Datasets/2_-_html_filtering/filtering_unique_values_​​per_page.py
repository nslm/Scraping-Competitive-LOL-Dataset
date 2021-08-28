from bs4 import BeautifulSoup as bs
import pandas as pd
from re import sub as gsub

df = pd.read_csv('./2_-_html_filtering/web_pages_html.csv')
df1 = df[['tempo_do_jogo', 'data', 'resultado_blue', 'resultado_red', 'gold_blue', 'gold_red', 'kills_blue', 'kills_red', 'frist_bloods', 'frist_towers', 'valor_max_do_grafico']]
# columns names:
# url, tempo_do_jogo, data, resultado_blue, resultado_red, gold_blue, gold_red, 
# kills_blue, kills_red, frist_bloods, frist_towers, sumario_inf_blue, sumarios_inf_red, 
# valor_max_do_grafico, tables, html_do_grafico, html_do_mapa
fb = df1['frist_bloods']
ft = df1['frist_towers']
g_blue = df1['gold_blue']
g_red = df1['gold_red']
r_blue = df1['resultado_blue']
r_red = df1['resultado_red']
vm = df1['valor_max_do_grafico']
sumario_blue = df['sumario_inf_blue']
sumario_red = df['sumarios_inf_red']

def filtro_g(str):
    str = gsub('mil','k', str)
    str = gsub(' ','', str)
    return str

def filtro_r(str):
    str = gsub('VITÓRIA', 'VICTORY', str)
    str = gsub('VITORIA', 'VICTORY', str)
    str = gsub('DERROTA', 'DEFEAT', str)
    return str

def valores_unicos_s(sumarios):
    towers = []
    inibs =[]
    barons = []
    drakes = []
    heralds = []
    for sumario in sumarios:
        soup = bs(sumario, 'html.parser')
        valores = soup.find_all('span')
        towers.append(valores[0].contents[0])
        inibs.append(valores[1].contents[0]) 
        barons.append(valores[2].contents[0])
        drakes.append(valores[3].contents[0])
        heralds.append(valores[4].contents[0])
    return [towers, inibs, barons, drakes, heralds]


for i in range(0, len(fb)):
    r_blue[i] = filtro_r(str(r_blue[i]))
    r_red[i] = filtro_r(str(r_red[i]))
    g_blue[i] = filtro_g(str(g_blue[i]))
    g_red[i] = filtro_g(str(g_red[i]))
    vm[i] = filtro_g(str(vm[i]))
    fb[i] = gsub('First Blood: ', '', str(fb[i]))
    ft[i] = gsub('First Tower Destroyed: ', '', str(ft[i]))
    ft[i] = gsub('Primeira torre destruída: ', '', str(ft[i]))

lista_su_blue = valores_unicos_s(sumario_blue)
lista_su_red = valores_unicos_s(sumario_red)
df1['torres_destruidos_blue'] = lista_su_blue[0]
df1['torres_destruidos_red'] = lista_su_red[0]
df1['inibs_destruidos_blue'] = lista_su_blue[1]
df1['inibs_destruidos_red'] = lista_su_red[1]
df1['barons_blue'] = lista_su_blue[2]
df1['barons_red'] = lista_su_red[2]
df1['drake_blue'] = lista_su_blue[3]
df1['drake_red'] = lista_su_red[3]
df1['heralds_blue'] = lista_su_blue[4]
df1['heralds_red'] = lista_su_red[4]
    

df1.to_csv('Valore_unicos_por_pagina_filtrados.csv')
