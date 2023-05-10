import os
import sys
import django
import requests
from bs4 import BeautifulSoup, Comment
import csv
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nba_stats.settings')
django.setup()

from nba_data.models import PlayerShotChartData

player_name = 'LeBron James'
season = 2016
url = 'https://www.basketball-reference.com/players/j/jamesle01/shooting/' + str(season)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the comment containing the shot chart
comment = soup.find(string=lambda text: isinstance(text, Comment) and "div_shot-chart" in text)
shot_chart_soup = BeautifulSoup(comment, "html.parser")

# Now you can find the shot chart in the parsed comment
shot_chart = shot_chart_soup.find("div", {"id": "shot-wrapper"})

shots = shot_chart.find_all("div", {"class": ["tooltip make", "tooltip miss"]})

team = 'CLE'  # You might want to find a way to get this from the webpage

# save data to database and CSV
shot_chart_data = []

for shot_div in shots:
    # Parse shot data
    style_values = shot_div['style'].split(';')
    top_value = int(style_values[0].split(':')[1].replace('px', '').strip())
    left_value = int(style_values[1].split(':')[1].replace('px', '').strip())

     # Parse tip attribute
    tip_parts = shot_div['tip'].split('<br>')

    # Within your loop:
    date_and_opponent = re.split(' at | vs ', tip_parts[0])
    date = date_and_opponent[0].strip().split(',')[0] + ',' + date_and_opponent[0].strip().split(',')[1]
    opponent = date_and_opponent[1].strip()

    quarter_and_time = tip_parts[1].split(',')
    quarter = quarter_and_time[0].strip()
    time_remaining = quarter_and_time[1].strip().split(' ')[0]

    result_and_type_and_distance = tip_parts[2].split(' ')
    result = result_and_type_and_distance[0].strip() == 'Made'
    shot_type = int(result_and_type_and_distance[1][0])
    distance_ft = int(result_and_type_and_distance[-2].strip())

    team_score_and_opponent_score = tip_parts[3].split(' ')[-1].split('-')
    team_score = int(team_score_and_opponent_score[0].strip())
    opponent_score = int(team_score_and_opponent_score[1].strip())

    lead = team_score > opponent_score

    shot_chart_row = {
        'player_name': player_name,
        'top': top_value,
        'left': left_value,
        'date': date,
        'qtr': quarter,
        'time_remaining': time_remaining,
        'result': result,
        'shot_type': shot_type,
        'distance_ft': distance_ft,
        'lead': lead,
        'lebron_team_score': team_score,
        'opponent_team_score': opponent_score,
        'opponent': opponent,
        'team': team,
        'season': season
    }
    shot_chart_data.append(shot_chart_row)

    # shot_chart_entry = PlayerShotChartData(**shot_chart_row)
    # shot_chart_entry.save()

# save as CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_output_path = os.path.join(script_dir, '..', 'data', f'{player_name}_{season}_shot_chart_output.csv')
with open(csv_output_path, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=shot_chart_data[0].keys())
    writer.writeheader()
    for row in shot_chart_data:
        writer.writerow(row)

print('success')