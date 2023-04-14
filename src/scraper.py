import requests
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/teams/HOU/2018.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"id": "per_game"})
rows = table.find_all("tr")


# print(rows)