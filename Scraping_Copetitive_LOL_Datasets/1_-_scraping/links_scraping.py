import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url1 = "https://lol.fandom.com/wiki/CBLOL/2017_Season/Split_1"
url2 = "https://lol.fandom.com/wiki/CBLOL/2017_Season/Split_2"
url3 = "https://lol.fandom.com/wiki/CBLOL/2018_Season/Split_1"
url4 = "https://lol.fandom.com/wiki/CBLOL/2018_Season/Split_2"
url5 = "https://lol.fandom.com/wiki/CBLOL/2019_Season/Split_1"
url6 = "https://lol.fandom.com/wiki/CBLOL/2019_Season/Split_2"
url7 = "https://lol.fandom.com/wiki/CBLOL/2020_Season/Split_1"
url8 = "https://lol.fandom.com/wiki/CBLOL/2020_Season/Split_2"
url9 = "https://lol.fandom.com/wiki/CBLOL/2021_Season/Split_1"
url10 = "https://lol.fandom.com/wiki/CBLOL/2021_Season/Split_2"

urls = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10]

links_filtrados = []

for url in urls:

    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a', href=True)]

    for i in links:
        if "https://matchhistory" in i or "http://matchhistory" in i:
            links_filtrados.append(i)

print(len(links_filtrados))


print(links_filtrados)

df = pd.DataFrame(links_filtrados)

df.to_csv('./2_-_html_filtering/links_to_scraping.csv')