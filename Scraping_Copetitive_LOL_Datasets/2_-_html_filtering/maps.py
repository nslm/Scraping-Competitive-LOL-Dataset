from bs4 import BeautifulSoup as bs
import pandas as pd

df = pd.read_csv('./2_-_html_filtering/web_pages_html.csv')
valores_mapas = df[['html_do_mapa']]


col_names = ['Data', 'Time', 'Player', 'Player_tag', 'KDA', 'Largest Killing Spree' 'Largest Multi Kill', 'First Blood', 'Total Damage to Champions', 'Physical Damage to Champions', 'Magic Damage to Champions', 'True Damage to Champions', 'Total Damage Dealt', 'Physical Damage Dealt', 'Magic Damage Dealt', 'True Damage Dealt', 'Largest Critical Strike', 'Total Damage to Objectives', 'Total Damage to Turrets', 'Damage Healed', 'Damage Taken', 'Physical Damage Taken', 'Magic Damage Taken', 'True Damage Taken', 'Wards Placed', 'Wards Destroyed', 'Stealth Wards Purchased', 'Control Wards Purchased', 'Gold Earned', 'Gold Spent', 'Minions Killed', 'Neutral Minions Killed', "Neutral Minions Killed in Team's Jungle", 'Neutral Minions Killed in Enemy Jungle', 'Team_Towers_Destroyed', 'Team_Inhibitor_Destroyed', 'Team_barons','Team_Drakes','Team_heralds', 'Team_side']
print(len(col_names))