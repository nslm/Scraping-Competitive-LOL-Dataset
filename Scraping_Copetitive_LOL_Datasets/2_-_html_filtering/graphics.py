from bs4 import BeautifulSoup as bs
import pandas as pd

df = pd.read_csv('./2_-_html_filtering/web_pages_html.csv')
df2 = pd.read_csv('./cblol_2018-2021.csv')
valores_max = df2[['valor_max_do_grafico']]
valores_graficos = df[['html_do_grafico']]