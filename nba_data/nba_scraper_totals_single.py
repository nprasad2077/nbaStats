import os
import sys
import django
import requests
from bs4 import BeautifulSoup
import csv
import json
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba_stats.settings')
django.setup()

from nba_data.models import PlayerTotalsData


season = input('What season? ')
team = input('What team?')

url_make = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '.html'
response = requests.get(url_make)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"id": "totals"})

if table is None:
    print(f"Table not found for team {team} and season {season}.")
    # sys.exit(1)
    # continue

header_row = table.find("thead").find("tr")
rows = table.find("tbody").find_all("tr")


# Extract coloumn headers
headers = [col.text.strip() for col in header_row.find_all("th")][1:]
headers.extend(['team', 'season'])  # Add 'team' and 'season' fields to headers

# Extract rows as dictionaries
data = []
for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    row_dict = {header: (None if col == "" else col) for header, col in zip(headers, cols)}
    row_dict['team'] = team
    row_dict['season'] = season
    data.append(row_dict)


# locate current directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# save as CSV file
csv_output_path = os.path.join(script_dir, '..', 'data', f'{team}_{season}_totals_output.csv')
with open(csv_output_path, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Save as JSON
json_output_path = os.path.join(script_dir, '..', 'data', f'{team}_{season}_totals_output.json')
with open(json_output_path, 'w') as jsonfile:
    json.dump(data, jsonfile)

# save data to database
for row in data:
    player_data = PlayerTotalsData(
        player_name = row['Player'],
        age = row['Age'],
        games = row['G'],
        games_started = row['GS'],
        minutes_played = row['MP'],
        field_goals = row['FG'],
        field_attempts = row['FGA'],
        field_percent = row['FG%'],
        three_fg = row['3P'],
        three_attempts = row['3PA'],
        three_percent = row['3P%'],
        two_fg = row['2P'],
        two_attempts = row['2PA'],
        two_percent = row['2P%'],
        effect_fg_percent = row['eFG%'],
        ft = row['FT'],
        fta = row['FTA'],
        ft_percent = row['FT%'],
        ORB= row['ORB'],
        DRB = row['DRB'],
        TRB = row['TRB'],
        AST = row['AST'],
        STL = row['STL'],
        BLK = row['BLK'],
        TOV = row['TOV'],
        PF = row['PF'],
        PTS = row['PTS'],
        team = row['team'],
        season = row['season'],
    )
    player_data.save()

print('success')
        

    