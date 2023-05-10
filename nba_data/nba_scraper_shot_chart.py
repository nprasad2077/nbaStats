import requests
from bs4 import BeautifulSoup, Comment

url = 'https://www.basketball-reference.com/players/j/jamesle01/shooting/2016'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the comment containing the shot chart
comment = soup.find(string=lambda text: isinstance(text, Comment) and "div_shot-chart" in text)

if comment:  # Make sure we've found the comment before we try to parse it
    shot_chart_soup = BeautifulSoup(comment, "html.parser")

    # Now you can find the shot chart in the parsed comment
    shot_chart = shot_chart_soup.find("div", {"id": "div_shot-chart"})

    if shot_chart:  # Check that we've found the shot chart
        shots = shot_chart.find_all("div")

        for shot in shots:
            print(shot)

    else:
        print('Shot chart not found')
else:
    print('Comment not found')
