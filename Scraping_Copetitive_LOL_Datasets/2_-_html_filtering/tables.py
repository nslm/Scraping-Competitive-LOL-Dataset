from bs4 import BeautifulSoup as bs
import pandas as pd

df = pd.read_csv('./2_-_html_filtering/web_pages_html.csv')
df2 = pd.read_csv('./cblol_2018-2021.csv')
tables = df[['tables']]
names = df[['names']]

list_players = []
list_players_team = []

for i in range(0,len(names)):
    htmls = str(names.loc[i][0])
    htmls = htmls.split(';;;;;')
    list_player_per_game = []
    list_player_per_game_team = []

    for j in range(0,len(htmls)):
        soup = bs(htmls[j], 'html.parser')
        list_names = soup.find('span')

        if list_names != None:
            list_names = list_names.contents[0]
            list_names_team = list_names.split(' ')[1]
            list_player_per_game.append(list_names)
            list_player_per_game_team.append(list_names_team)
        else:
            
            list_player_per_game.append(None)
            list_player_per_game_team.append(None)

    list_players.append(list_player_per_game)
    list_players_team.append(list_player_per_game_team)

list_rows = []
for c in range(0,len(names)):
    html = str(tables.loc[c][0])
    soup = bs(html, 'html.parser')
    html_rows = soup.find_all('tr', {'class':'grid-row'})
    rows = [list_players_team[c], list_players[c]]
    
    for i in range(0,30):
        if len(html_rows) == 30:
            row = html_rows[i].find_all('div')            
            for j in range(0,11):
                row[j]= row[j].contents[0]
            del row[0]
            rows.append(row)
        else:
            rows.append([None,None,None,None,None,None,None,None,None,None])
    list_rows.append(rows)

table = list_rows
col_names = ['Data', 'Time', 'Player', 'Player_tag', 'KDA', 'Largest Killing Spree' 'Largest Multi Kill', 'First Blood', 'Total Damage to Champions', 'Physical Damage to Champions', 'Magic Damage to Champions', 'True Damage to Champions', 'Total Damage Dealt', 'Physical Damage Dealt', 'Magic Damage Dealt', 'True Damage Dealt', 'Largest Critical Strike', 'Total Damage to Objectives', 'Total Damage to Turrets', 'Damage Healed', 'Damage Taken', 'Physical Damage Taken', 'Magic Damage Taken', 'True Damage Taken', 'Wards Placed', 'Wards Destroyed', 'Stealth Wards Purchased', 'Control Wards Purchased', 'Gold Earned', 'Gold Spent', 'Minions Killed', 'Neutral Minions Killed', "Neutral Minions Killed in Team's Jungle", 'Neutral Minions Killed in Enemy Jungle', 'Team Towers Destroyed', 'Team Inhibitor Destroyed', 'Team barons','Team Drakes','Team heralds', 'Team side']

Player = []
Player_tag = []
KDA = []
Largest_Killing_Spree = []
Largest_Multi_Kill = []
First_Blood = []
Total_Damage_to_Champions = []
Physical_Damage_to_Champions = []
Magic_Damage_to_Champions = []
True_Damage_to_Champions = []
Total_Damage_Dealt = []
Physical_Damage_Dealt = []
Magic_Damage_Dealt = []
True_Damage_Dealt = []
Largest_Critical_Strike = []
Total_Damage_to_Objectives = []
Total_Damage_to_Turrets  = []
Damage_Healed = []
Damage_Taken = []
Physical_Damage_Taken = []
Magic_Damage_Taken = []
True_Damage_Taken = []
Wards_Placed = []
Wards_Destroyed = []
Stealth_Wards_Purchased = []
Control_Wards_Purchased = []
Gold_Earned = []
Gold_Spent = []
Minions_Killed = []
Neutral_Minions_Killed = []
Neutral_Minions_Killed_in_Teams_Jungle = []
Neutral_Minions_Killed_in_Enemy_Jungle = []

cols = [Player, Player_tag, KDA, Largest_Killing_Spree, Largest_Multi_Kill, First_Blood, Total_Damage_to_Champions, Physical_Damage_to_Champions, Magic_Damage_to_Champions, True_Damage_to_Champions, Total_Damage_Dealt, Physical_Damage_Dealt, Magic_Damage_Dealt, True_Damage_Dealt, Largest_Critical_Strike, Total_Damage_to_Objectives, Total_Damage_to_Turrets , Damage_Healed, Damage_Taken, Physical_Damage_Taken, Magic_Damage_Taken, True_Damage_Taken, Wards_Placed, Wards_Destroyed, Stealth_Wards_Purchased, Control_Wards_Purchased, Gold_Earned, Gold_Spent, Minions_Killed, Neutral_Minions_Killed, Neutral_Minions_Killed_in_Teams_Jungle, Neutral_Minions_Killed_in_Enemy_Jungle]


for c in range(0,len(table)):
    for i in range(0,len(table[c])):
        for j in range(0,len(table[c][i])):
            if table[c][i][j] != None:
                cols[i].append(table[c][i][j])
            else:
                cols[i].append(None)

def blue_more_red(blue, red):
    blue_more_red = []
    for i in range(0,len(red)):
        for j in range(0,5):
            blue_more_red.append(blue[i])
        for j in range(0,5):
            blue_more_red.append(red[i])

data = df2['data']
time = df2['tempo_do_jogo']
resultado_blue = df2['resultado_blue']
resultado_red = df2['resultado_red']
team_towers_Destroyed_blue = df2['torres_destruidos_blue']
team_towers_Destroyed_red = df2['torres_destruidos_red']
team_inhibitor_Destroyed_blue = df2['inibs_destruidos_blue']
team_inhibitor_Destroyed_red = df2['inibs_destruidos_red']
team_barons_blue = df2['barons_blue']
team_barons_red = df2['barons_red']
team_drakes_blue = df2['drake_blue']
team_drakes_red = df2['drake_red']
team_heralds_blue = df2['heralds_blue']
team_heralds_red = df2['heralds_red']

Data = []
Time = []
Win = []
Team_Towers_Destroyed = []
Team_Inhibitor_Destroyed = []
Team_Barons = []
Team_Drakes = []
Team_Heralds = []
Team_Side = []

for i in range(0,len(data)):
    for j in range(0,10):
        Data.append(data[i])
        Time.append(time[i])

    for j in range(0,5):
        Team_Towers_Destroyed.append(team_towers_Destroyed_blue[i])
        Team_Inhibitor_Destroyed.append(team_inhibitor_Destroyed_blue[i])
        Team_Barons.append(team_barons_blue[i])
        Team_Drakes.append(team_drakes_blue[i])
        Team_Heralds.append(team_heralds_blue[i])

    for j in range(0,5):
        Team_Towers_Destroyed.append(team_towers_Destroyed_red[i])
        Team_Inhibitor_Destroyed.append(team_inhibitor_Destroyed_red[i])
        Team_Barons.append(team_barons_red[i])
        Team_Drakes.append(team_drakes_red[i])
        Team_Heralds.append(team_heralds_red[i])
    
    if resultado_blue[i] == 'VICTORY':
        win = 1
    elif resultado_blue[i] == 'DEFEAT':
        win = 0

    for j in range(0,5):
        resultado_blue[i]
        Win.append(win)
    
    
    for j in range(0,5):
        resultado_red[i]
        Win.append(win)

    for j in range(0,5):
        Team_Side.append('Blue')
    for j in range(0,5):
        Team_Side.append('Red')


dataframe = pd.DataFrame(zip(Data, Time, Player, Player_tag, KDA, Largest_Killing_Spree, Largest_Multi_Kill, First_Blood, Total_Damage_to_Champions, Physical_Damage_to_Champions, Magic_Damage_to_Champions, True_Damage_to_Champions, Total_Damage_Dealt, Physical_Damage_Dealt, Magic_Damage_Dealt, True_Damage_Dealt, Largest_Critical_Strike, Total_Damage_to_Objectives, Total_Damage_to_Turrets , Damage_Healed, Damage_Taken, Physical_Damage_Taken, Magic_Damage_Taken, True_Damage_Taken, Wards_Placed, Wards_Destroyed, Stealth_Wards_Purchased, Control_Wards_Purchased, Gold_Earned, Gold_Spent, Minions_Killed, Neutral_Minions_Killed, Neutral_Minions_Killed_in_Teams_Jungle, Neutral_Minions_Killed_in_Enemy_Jungle, Team_Towers_Destroyed, Team_Inhibitor_Destroyed, Team_Barons,Team_Drakes, Team_Heralds, Team_Side), columns=col_names)

dataframe.to_csv('cblol_2018-2021_by_player.csv')