# NBA Stats API 0.1 Beta

## Introduction

This documentation provides the necessary information to use the NBA Stats API. These APIs provide access to NBA season and playoff totals, advanced statistics, shot chart data, and more.

---

### Base URL

All URLs referenced in this documentation use the following base URL:

> https://nba-stats-db.herokuapp.com/

### Endpoints

Top 20 Scorers by Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/total/season/2023/

Success Response:

`Code: 200`

Content:
```
{
    "count": 20,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 40,
            "player_name": "Jayson Tatum",
            "age": 24,
            "games": 74,
            "games_started": 74,
            "minutes_played": 2732,
            "field_goals": 727,
            "field_attempts": 1559,
            "field_percent": "0.466",
            "three_fg": 240,
            "three_attempts": 686,
            "three_percent": "0.350",
            "two_fg": 487,
            "two_attempts": 873,
            "two_percent": "0.558",
            "effect_fg_percent": "0.543",
            "ft": 531,
            "fta": 622,
            "ft_percent": "0.854",
            "ORB": 78,
            "DRB": 571,
            "TRB": 649,
            "AST": 342,
            "STL": 78,
            "BLK": 51,
            "TOV": 213,
            "PF": 160,
            "PTS": 2225,
            "team": "BOS",
            "season": 2023
        },
        {
            "id": 20,
            "player_name": "Joel Embiid",
            "age": 28,
            "games": 66,
            "games_started": 66,
            "minutes_played": 2284,
            "field_goals": 728,
            "field_attempts": 1328,
            "field_percent": "0.548",
            "three_fg": 66,
            "three_attempts": 200,
            "three_percent": "0.330",
            "two_fg": 662,
            "two_attempts": 1128,
            "two_percent": "0.587",
            "effect_fg_percent": "0.573",
            "ft": 661,
            "fta": 771,
            "ft_percent": "0.857",
            "ORB": 113,
            "DRB": 557,
            "TRB": 670,
            "AST": 274,
            "STL": 66,
            "BLK": 112,
            "TOV": 226,
            "PF": 205,
            "PTS": 2183,
            "team": "PHI",
            "season": 2023
        },
	...
	]
}		

```

Top 20 Scorers in Playoffs
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/playoffs/2022/

Success Response:

`Code: 200`

Content:
```
{
    "count": 20,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 16,
            "player_name": "Jayson Tatum",
            "age": 23,
            "games": 24,
            "games_started": 24,
            "minutes_played": 983,
            "field_goals": 201,
            "field_attempts": 472,
            "field_percent": "0.426",
            "three_fg": 77,
            "three_attempts": 196,
            "three_percent": "0.393",
            "two_fg": 124,
            "two_attempts": 276,
            "two_percent": "0.449",
            "effect_fg_percent": "0.507",
            "ft": 136,
            "fta": 170,
            "ft_percent": "0.800",
            "ORB": 24,
            "DRB": 137,
            "TRB": 161,
            "AST": 148,
            "STL": 29,
            "BLK": 21,
            "TOV": 100,
            "PF": 72,
            "PTS": 615,
            "team": "BOS",
            "season": 2022
        },
        {
            "id": 178,
            "player_name": "Stephen Curry",
            "age": 33,
            "games": 22,
            "games_started": 18,
            "minutes_played": 764,
            "field_goals": 202,
            "field_attempts": 440,
            "field_percent": "0.459",
            "three_fg": 91,
            "three_attempts": 229,
            "three_percent": "0.397",
            "two_fg": 111,
            "two_attempts": 211,
            "two_percent": "0.526",
            "effect_fg_percent": "0.563",
            "ft": 107,
            "fta": 129,
            "ft_percent": "0.829",
            "ORB": 11,
            "DRB": 104,
            "TRB": 115,
            "AST": 129,
            "STL": 29,
            "BLK": 8,
            "TOV": 57,
            "PF": 59,
            "PTS": 602,
            "team": "GSW",
            "season": 2022
        },
	...
	]
}		

```

Top 20 Assists by Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/top_assists/totals/2023/

Success Response:

`Code: 200`

Content:
```
{
    "count": 20,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 529,
            "player_name": "Trae Young",
            "age": 24,
            "games": 73,
            "games_started": 73,
            "minutes_played": 2541,
            "field_goals": 597,
            "field_attempts": 1390,
            "field_percent": "0.429",
            "three_fg": 154,
            "three_attempts": 460,
            "three_percent": "0.335",
            "two_fg": 443,
            "two_attempts": 930,
            "two_percent": "0.476",
            "effect_fg_percent": "0.485",
            "ft": 566,
            "fta": 639,
            "ft_percent": "0.886",
            "ORB": 56,
            "DRB": 161,
            "TRB": 217,
            "AST": 741,
            "STL": 80,
            "BLK": 9,
            "TOV": 300,
            "PF": 104,
            "PTS": 1914,
            "team": "ATL",
            "season": 2023
        },
        {
            "id": 203,
            "player_name": "Nikola Jokić",
            "age": 27,
            "games": 69,
            "games_started": 69,
            "minutes_played": 2323,
            "field_goals": 646,
            "field_attempts": 1022,
            "field_percent": "0.632",
            "three_fg": 57,
            "three_attempts": 149,
            "three_percent": "0.383",
            "two_fg": 589,
            "two_attempts": 873,
            "two_percent": "0.675",
            "effect_fg_percent": "0.660",
            "ft": 341,
            "fta": 415,
            "ft_percent": "0.822",
            "ORB": 167,
            "DRB": 650,
            "TRB": 817,
            "AST": 678,
            "STL": 87,
            "BLK": 47,
            "TOV": 247,
            "PF": 174,
            "PTS": 1690,
            "team": "DEN",
            "season": 2023
        },
	...
	]
}		

```

Top 20 Assists in Playoffs
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/top_assists/playoffs/2022/


Success Response:

`Code: 200`

Content:
```
{
    "count": 20,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 16,
            "player_name": "Jayson Tatum",
            "age": 23,
            "games": 24,
            "games_started": 24,
            "minutes_played": 983,
            "field_goals": 201,
            "field_attempts": 472,
            "field_percent": "0.426",
            "three_fg": 77,
            "three_attempts": 196,
            "three_percent": "0.393",
            "two_fg": 124,
            "two_attempts": 276,
            "two_percent": "0.449",
            "effect_fg_percent": "0.507",
            "ft": 136,
            "fta": 170,
            "ft_percent": "0.800",
            "ORB": 24,
            "DRB": 137,
            "TRB": 161,
            "AST": 148,
            "STL": 29,
            "BLK": 21,
            "TOV": 100,
            "PF": 72,
            "PTS": 615,
            "team": "BOS",
            "season": 2022
        },
        {
            "id": 179,
            "player_name": "Draymond Green",
            "age": 31,
            "games": 22,
            "games_started": 22,
            "minutes_played": 703,
            "field_goals": 69,
            "field_attempts": 144,
            "field_percent": "0.479",
            "three_fg": 8,
            "three_attempts": 39,
            "three_percent": "0.205",
            "two_fg": 61,
            "two_attempts": 105,
            "two_percent": "0.581",
            "effect_fg_percent": "0.507",
            "ft": 30,
            "fta": 47,
            "ft_percent": "0.638",
            "ORB": 26,
            "DRB": 133,
            "TRB": 159,
            "AST": 138,
            "STL": 25,
            "BLK": 22,
            "TOV": 59,
            "PF": 87,
            "PTS": 176,
            "team": "GSW",
            "season": 2022
        },
	...
	]
}		

```

Top 20 Rebounders (Total Rebounds) by Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/top_rebounds/totals/2023/

Success Response:

`Code: 200`

Content:
```
{
    "count": 20,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 405,
            "player_name": "Domantas Sabonis",
            "age": 26,
            "games": 79,
            "games_started": 79,
            "minutes_played": 2736,
            "field_goals": 577,
            "field_attempts": 938,
            "field_percent": "0.615",
            "three_fg": 31,
            "three_attempts": 83,
            "three_percent": "0.373",
            "two_fg": 546,
            "two_attempts": 855,
            "two_percent": "0.639",
            "effect_fg_percent": "0.632",
            "ft": 325,
            "fta": 438,
            "ft_percent": "0.742",
            "ORB": 251,
            "DRB": 722,
            "TRB": 973,
            "AST": 573,
            "STL": 65,
            "BLK": 39,
            "TOV": 230,
            "PF": 279,
            "PTS": 1510,
            "team": "SAC",
            "season": 2023
        },
        {
            "id": 346,
            "player_name": "Nikola Vučević",
            "age": 32,
            "games": 82,
            "games_started": 82,
            "minutes_played": 2746,
            "field_goals": 597,
            "field_attempts": 1148,
            "field_percent": "0.520",
            "three_fg": 121,
            "three_attempts": 347,
            "three_percent": "0.349",
            "two_fg": 476,
            "two_attempts": 801,
            "two_percent": "0.594",
            "effect_fg_percent": "0.573",
            "ft": 132,
            "fta": 158,
            "ft_percent": "0.835",
            "ORB": 159,
            "DRB": 744,
            "TRB": 903,
            "AST": 265,
            "STL": 60,
            "BLK": 57,
            "TOV": 139,
            "PF": 179,
            "PTS": 1447,
            "team": "CHI",
            "season": 2023
        },
	...
	]
}		

```

## Plan

1. Data collection - Selenium - live data from dyanic websites. - Beautiful soap/scrapy - historical static data. - Live data - websocket connections or periodic updates.  
   &nbsp;

2. Backend API - Django (Python): A more comprehensive framework that includes an ORM and admin panel out-of-the-box. - Django REST Framework
   &nbsp;

3. Backend DB
   -Initially SQL lite, but it quickly met its limitations when trying to scrape data for 30 teams at once. It could not handle all the simulataneous connections.

   - PostgreSQL is the new DB.

4. Frontend - React/Redux - D3.js - Chart.js - Highcharts - Websockets or Server-Sent Events
   &nbsp;

5. Deployment
