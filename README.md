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
Code: 200
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

Top 20 Assists by Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/top_assists/totals/2023/

Top 20 Assists in Playoffs
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/top_assists/playoffs/2022/

Top 20 Rebounders (Total Rebounds) by Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/top_rebounds/2023/

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
