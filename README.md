# NBA Stats API 0.1 Beta

## Introduction

This documentation provides the necessary information to use the NBA Stats API. These APIs provide access to NBA season and playoff totals, advanced statistics, shot chart data, and more.

---

# [View API Documentation](https://documenter.getpostman.com/view/24232555/2s93shzpR3)



---


### Base URL

All URLs referenced in this documentation use the following base URL:

> https://nba-stats-db.herokuapp.com/

### Endpoint Examples

Top 20 Scorers by Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/playerdata/topscorers/total/season/2023/

Success Response:

`Code: 200`

Content:
```
{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
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
        {
            "id": 846,
            "player_name": "Nikola Jokić",
            "age": 26,
            "games": 74,
            "games_started": 74,
            "minutes_played": 2476,
            "field_goals": 764,
            "field_attempts": 1311,
            "field_percent": "0.583",
            "three_fg": 97,
            "three_attempts": 288,
            "three_percent": "0.337",
            "two_fg": 667,
            "two_attempts": 1023,
            "two_percent": "0.652",
            "effect_fg_percent": "0.620",
            "ft": 379,
            "fta": 468,
            "ft_percent": "0.810",
            "ORB": 206,
            "DRB": 813,
            "TRB": 1019,
            "AST": 584,
            "STL": 109,
            "BLK": 63,
            "TOV": 281,
            "PF": 191,
            "PTS": 2004,
            "team": "DEN",
            "season": 2022
        },
	...
	]
}		
```

All Players in Season
Method: `Get`

> https://nba-stats-db.herokuapp.com/api/playerdata/season/2023

Success Response:

`Code: 200`

Content:
```
{
    "count": 609,
    "next": "https://nba-stats-db.herokuapp.com/api/playerdata/season/2023/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "player_name": "Jalen Green",
            "age": 20,
            "games": 76,
            "games_started": 76,
            "minutes_played": 2602,
            "field_goals": 566,
            "field_attempts": 1359,
            "field_percent": "0.416",
            "three_fg": 187,
            "three_attempts": 554,
            "three_percent": "0.338",
            "two_fg": 379,
            "two_attempts": 805,
            "two_percent": "0.471",
            "effect_fg_percent": "0.485",
            "ft": 364,
            "fta": 463,
            "ft_percent": "0.786",
            "ORB": 43,
            "DRB": 241,
            "TRB": 284,
            "AST": 281,
            "STL": 59,
            "BLK": 18,
            "TOV": 200,
            "PF": 131,
            "PTS": 1683,
            "team": "HOU",
            "season": 2023
        },
        {
            "id": 2,
            "player_name": "Jabari Smith Jr.",
            "age": 19,
            "games": 79,
            "games_started": 79,
            "minutes_played": 2451,
            "field_goals": 364,
            "field_attempts": 892,
            "field_percent": "0.408",
            "three_fg": 120,
            "three_attempts": 391,
            "three_percent": "0.307",
            "two_fg": 244,
            "two_attempts": 501,
            "two_percent": "0.487",
            "effect_fg_percent": "0.475",
            "ft": 162,
            "fta": 206,
            "ft_percent": "0.786",
            "ORB": 122,
            "DRB": 447,
            "TRB": 569,
            "AST": 101,
            "STL": 43,
            "BLK": 74,
            "TOV": 104,
            "PF": 227,
            "PTS": 1010,
            "team": "HOU",
            "season": 2023
        },
	...
	]
}

```
## Reference

All statistics are referenced from [basketball-reference.com](https://www.basketball-reference.com/)
