import requests
from bs4 import BeautifulSoup
import csv
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

# add coloumn headers to the data list
data = [headers]

# extract rows of data into proper column with headers.

for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    data.append(cols)
    
    
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, '..', 'data', 'output.csv')

with open(output_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)