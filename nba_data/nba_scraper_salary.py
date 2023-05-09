import os
import sys
import django
import requests
from bs4 import BeautifulSoup, Comment
import csv
import json
import time
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba_stats.settings')
django.setup()

from nba_data.models import PlayerSalaryData

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


teams = ['HOU' ,'PHI', 'BOS', 'NYK', 'BRK', 'TOR', 'MEM', 'NOP', 'DAL', 'SAS', 'DEN', 'MIN', 'OKC', 'UTA', 'POR', 'MIL', 'CLE', 'CHI', 'IND', 'DET', 'SAC', 'PHO', 'GSW', 'LAC', 'LAL', 'MIA', 'ATL', 'WAS', 'ORL', 'CHO']
teams_test = ['HOU', 'PHI', 'BOS']

season = input('What season? ')

for team in teams_test:
    url_make = 'https://www.basketball-reference.com/teams/' + team + '/' + season + '.html'
    response = requests.get(url_make)
    
    soup = BeautifulSoup(response.text, "html.parser")

    comment = soup.find(string=lambda text: isinstance(text, Comment) and "salaries2" in text)
    table_soup = BeautifulSoup(comment, "html.parser")
    table = table_soup.find("table", {'class': 'suppress_all stats_table', 'id': 'salaries2'})

    if table is None:
        print(f"Table not found for team {team} and season {season}.")
        # sys.exit(1)
        continue

    header_row = table.find("thead").find("tr")
    rows = table.find("tbody").find_all("tr")


    # Extract coloumn headers
    headers = ['player_name']
    headers.extend([col.text.strip() for col in header_row.find_all("th")][2:])
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
    csv_output_path = os.path.join(script_dir, '..', 'data', f'{team}_{season}_player_salary_output.csv')
    with open(csv_output_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    # Save as JSON
    json_output_path = os.path.join(script_dir, '..', 'data', f'{team}_{season}_player_salary_output.json')
    with open(json_output_path, 'w') as jsonfile:
        json.dump(data, jsonfile)

    # save data to database
    
    # for row in data:
        
    #     row['Salary'] = int(row['Salary'].replace(',', '').replace('$', '')) if row['Salary'] else None
        
    #     player_data = PlayerSalaryData(
    #         player_name = row['player_name'],
    #         salary = row['Salary'],
    #         team = row['team'],
    #         season = row['season'],       
    #     )
    #     player_data.save()

print('success')
        

    