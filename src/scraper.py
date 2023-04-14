import requests
from bs4 import BeautifulSoup
import csv
import json
import os

url = 'https://www.basketball-reference.com/teams/HOU/2018.html'
response = requests.get(url)

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