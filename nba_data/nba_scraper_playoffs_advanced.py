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

from nba_data.models import PlayerPlayoffAdvancedData

# Change CHO to CHA 2014 and prior.
# Change NOP to NOH for 2013 and prior.
# Change OKC to SEA for 2008 and prior.
# Change NOH to NOK for 2007 and 2006
# Change NOK to NOH for 2005 and prior.
# Change NOH to CHH for 2002 and prior. NOLA did not have a team before 2003.
# Change WAS to WSB for 1997 and prior.
# Change BRK to NJN for 2012 and prior.
# Change MEM to VAN for 2001 and prior.
# Change LAC to SDC for 1984 and prior.


teams = ['HOU' ,'PHI', 'BOS', 'NYK', 'NJN', 'TOR', 'MEM', 'NOH', 'DAL', 'SAS', 'DEN', 'MIN', 'OKC', 'UTA', 'POR', 'MIL', 'CLE', 'CHI', 'IND', 'DET', 'SAC', 'PHO', 'GSW', 'LAC', 'LAL', 'MIA', 'ATL', 'WAS', 'ORL', 'CHA']

season = input('What season? ')

for team in teams:
    url_make = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '.html'
    response = requests.get(url_make)

    soup = BeautifulSoup(response.text, "html.parser")
    
    table = soup.find("table", {"id": "playoffs_advanced"})

    if table is None:
        print(f"Table not found for team {team} and season {season}.")
        # sys.exit(1)
        continue

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
    csv_output_path = os.path.join(script_dir, '..', 'data', f'{team}_{season}_playoffs_advanced_output.csv')
    with open(csv_output_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # Save as JSON
    json_output_path = os.path.join(script_dir, '..', 'data', f'{team}_{season}_playoffs_advanced_output.json')
    with open(json_output_path, 'w') as jsonfile:
        json.dump(data, jsonfile)

    # save data to database
    for row in data:
        player_data = PlayerPlayoffAdvancedData(
            player_name = row['Player'],
            age = row['Age'],
            games = row['G'],
            minutes_played = row['MP'],
            PER = row['PER'],
            TS_percent = row['TS%'],
            three_p_attempt_rate = row['3PAr'],
            ft_attempt_rate = row['FTr'],
            orb_percent = row['ORB%'],
            drb_percent = row['DRB%'],
            trb_percent = row['TRB%'],
            ast_percent = row['AST%'],
            stl_percent = row['STL%'],
            blk_percent = row['BLK%'],
            tov_percent = row['TOV%'],
            usg_percent = row['USG%'],
            ows = row['OWS'],
            dws = row['DWS'],
            ws = row['WS'],
            ws_per_48 = row['WS/48'],
            obpm = row['OBPM'],
            dbpm = row['DBPM'],
            bpm = row['BPM'],
            vorp = row['VORP'],
            team = row['team'],
            season = row['season'],
        )
        player_data.save()

print('success')
        

    