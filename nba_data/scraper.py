import requests
from bs4 import BeautifulSoup
import csv
import json
import os
from .models import PlayerData


team = input('What team? ')
season = input('What season? ')

url_make = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '.html'

url = 'https://www.basketball-reference.com/teams/HOU/2018.html'
lakers = 'https://www.basketball-reference.com/teams/LAL/2020.html'

response = requests.get(url_make)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"id": "per_game"})
# rows = table.find_all("tr")
header_row = table.find("thead").find("tr")
rows = table.find("tbody").find_all("tr")

# Extract coloumn headers
headers = [col.text.strip() for col in header_row.find_all("th")][1:]


# extract rows as dictionaries
data = []
for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    row_dict = dict(zip(headers, cols))
    data.append(row_dict)
    
## locate current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

## CSV file

csv_output_path = os.path.join(script_dir, '..', 'data', 'output.csv')

with open(csv_output_path, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames =headers)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Save as JSON

json_output_path = os.path.join(script_dir, '..', 'data', 'output.json')
with open(json_output_path, 'w') as jsonfile:
    json.dump(data, jsonfile)
    

# save data to database

for row in data:
    player_data = PlayerData(
        name=row['name'],
        age=row['age'],
        games=row['games'],
        games_started=row['games_started'],
        minutes_pg=row['minutes_pg'],
        field_goals=row['field_goals'],
        field_attempts=row['field_attempts'],
        field_percent=row['field_percent'],
        three_fg=row['three_fg'],
        three_attempts=row['three_attempts'],
        three_percent=row['three_percent'],
        two_fg=row['two_fg'],
        two_attempts=row['two_attempts'],
        two_percent=row['two_percent'],
        effect_fg_percent=row['effect_fg_percent'],
        ft=row['ft'],
        fta=row['fta'],
        ft_percent=row['ft_percent'],
        ORB=row['ORB'],
        DRB=row['DRB'],
        TRB=row['TRB'],
        AST=row['AST'],
        STL=row['STL'],
        BLK=row['BLK'],
        TOV=row['TOV'],
        PF=row['PF'],
        PTS=row['PTS'],
    )
    player_data.save()