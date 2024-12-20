# NBA Stats API 0.1 Beta

## ‼️View the new and updated REST API [here.](http://rest.nbaapi.com/index.html) 🔎✅🏀📎👽👾🤖🏆
## ‼️View the new and updated GraphQL API [here.](https://github.com/nprasad2077/NBA_GraphQL) 🏀⛹️

## Introduction

This documentation provides the necessary information to use the NBA Stats API. These APIs provide access to NBA season and playoff totals, advanced statistics, shot chart data, and more. Stats are cross-referenced with [basketball-reference.com](https://www.basketball-reference.com/) and [NBA.com](https://www.nba.com/stats).

---
[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/25652688-483c72bc-2588-4b7e-b9f9-30c3f5f2ebcc?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25652688-483c72bc-2588-4b7e-b9f9-30c3f5f2ebcc%26entityType%3Dcollection%26workspaceId%3Dbb6fcb02-8388-4ce0-8623-63480a6dc153)

## [View 2025 API Documentation](https://www.postman.com/solar-meadow-682296/nba-stats/collection/eti4u40/nba-stats-api)

---

# NBA Player Data API

This API provides endpoints to query NBA player statistics, including both "Totals" data and "Advanced" statistical data. Each endpoint supports filtering, sorting, and pagination options to help you retrieve the data you need.

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://god.gw.postman.com/run-collection/25652688-483c72bc-2588-4b7e-b9f9-30c3f5f2ebcc?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25652688-483c72bc-2588-4b7e-b9f9-30c3f5f2ebcc%26entityType%3Dcollection%26workspaceId%3Dbb6fcb02-8388-4ce0-8623-63480a6dc153)

## Base URL

All endpoints are served from the base URL:

```
http://rest.nbaapi.com
```

## Authentication

No authentication is currently required for these endpoints.

## Endpoints Overview

- **Player Data Totals** (`/playerdatatotals`)

  Provides season-based totals such as points, assists, games played, and more.

- **Player Data Advanced** (`/playerdataadvanced`)

  Provides advanced player metrics such as Player Efficiency Rating (PER), True Shooting Percentage (TS%), Usage Percentage, Win Shares, and other advanced stats.

Both endpoints offer similar querying patterns and filtering options.

---

## Common Query Parameters

For both Totals and Advanced endpoints, the following query parameters are available for the `/query` routes:

- **playerName** *(string, optional)*: Filter results to players whose name matches or partially matches the provided string.
- **season** *(int, optional)*: Filter by a specific season (e.g., `2025`).
- **team** *(string, optional)*: Filter by a team abbreviation (partial matches allowed).
- **playerId** *(string, optional)*: Filter by a player's unique ID (partial matches allowed).

**Sorting Options:**

- **sortBy** *(string, optional)*: Field name to sort results by. Varies by endpoint.
- **ascending** *(bool, optional)*: Set to `true` (default) for ascending order or `false` for descending order.

**Pagination:**
- **pageNumber** *(int, optional)*: Page number to retrieve (default is 1).
- **pageSize** *(int, optional)*: Number of records per page (default is 10).

If no data matches your query, the response will be `404 Not Found`.

---

## Player Data Totals Endpoints

**Base Route:** `/playerdatatotals`

### 1. Query Player Totals

**GET** `/playerdatatotals/query`

**Description:**  
Retrieves a filtered and/or sorted list of player totals data.

**Query Parameters:**
- `playerName` (string)
- `season` (int)
- `team` (string)
- `playerId` (string)
- `sortBy` (string): Can be `PlayerName`, `Season`, `Team`, `Points`, `Assists`, `Games`, `TotalRb`, `Blocks`, `Steals`.
- `ascending` (bool): Default `true`.
- `pageNumber` (int): Default `1`.
- `pageSize` (int): Default `10`.

**Response:**  
`200 OK` with a JSON array of `PlayerDataTotals` objects, or `404 Not Found` if no records match.

**Example Request:**

```bash
curl -X GET \
  'http://rest.nbaapi.com/api/PlayerDataTotals/query?season=2025&team=BOS&sortBy=PlayerName&ascending=true&pageNumber=1&pageSize=10' \
  -H 'accept: text/plain'
```

**Example Response:**
```json
[
  {
    "id": 18905,
    "playerName": "Al Horford",
    "position": "C",
    "age": 38,
    "games": 19,
    "gamesStarted": 18,
    "minutesPg": 532,
    "fieldGoals": 64,
    "fieldAttempts": 137,
    "fieldPercent": 0.467,
    "threeFg": 41,
    "threeAttempts": 101,
    "threePercent": 0.406,
    "twoFg": 23,
    "twoAttempts": 36,
    "twoPercent": 0.639,
    "effectFgPercent": 0.617,
    "ft": 6,
    "ftAttempts": 6,
    "ftPercent": 1,
    "offensiveRb": 16,
    "defensiveRb": 85,
    "totalRb": 101,
    "assists": 44,
    "steals": 14,
    "blocks": 17,
    "turnovers": 19,
    "personalFouls": 31,
    "points": 175,
    "team": "BOS",
    "season": 2025,
    "playerId": "horfoal01"
  },
  ...
]
```

*(Response truncated for brevity.)*

### 2. Get Player Totals by Name

**GET** `/playerdatatotals/name/{playerName}`

**Description:**  
Retrieve all totals data for players whose names match or partially match the given `playerName`.

**Response:**  
`200 OK` with a JSON array of `PlayerDataTotals` objects or `404 Not Found`.

### 3. Get Player Totals by Season

**GET** `/playerdatatotals/season/{season}`

**Description:**  
Retrieve all player totals for a given season.

### 4. Get Player Totals by Player ID

**GET** `/playerdatatotals/playerid/{playerId}`

**Description:**  
Retrieve all totals data for a player by their unique or partial `playerId`.

### 5. Get Player Totals by Team

**GET** `/playerdatatotals/team/{team}`

**Description:**  
Retrieve totals for all players who played on a given team.

### 6. Count of All Player Totals Records

**GET** `/playerdatatotals/count`

**Description:**  
Retrieve an integer count of all available player totals records.

---

## Player Data Advanced Endpoints

**Base Route:** `/playerdataadvanced`

### 1. Query Player Advanced Data

**GET** `/playerdataadvanced/query`

**Description:**  
Retrieve a filtered and/or sorted list of advanced player stats.

**Query Parameters:**
- `playerName` (string)
- `season` (int)
- `team` (string)
- `playerId` (string)
- `sortBy` (string): Possible fields include `PlayerName`, `Season`, `Team`, `Games`, `PER`, `TSPercent`, `TotalRBPercent`, `AssistPercent`, `StealPercent`, `BlockPercent`, `TurnoverPercent`, `UsagePercent`, `WinShares`, `Box`, `VORP`.
- `ascending` (bool): Default `true`.
- `pageNumber` (int): Default `1`.
- `pageSize` (int): Default `10`.

**Response:**  
`200 OK` with a JSON array of `PlayerDataAdvanced` objects, or `404 Not Found` if no records match.

**Example Request:**
```bash
curl -X GET \
  'http://rest.nbaapi.com/api/PlayerDataAdvanced/query?playerName=James%20Harden&team=HOU&sortBy=WinShares&ascending=false&pageNumber=1&pageSize=10' \
  -H 'accept: text/plain'
```

**Example Response:**
```json
[
  {
    "id": 5645,
    "playerName": "James Harden",
    "position": "SG",
    "age": 25,
    "games": 81,
    "minutesPlayed": 2981,
    "per": 26.7,
    "tsPercent": 0.605,
    "threePAR": 0.378,
    "ftr": 0.561,
    "offensiveRBPercent": 2.8,
    "defensiveRBPercent": 14.2,
    "totalRBPercent": 8.5,
    "assistPercent": 34.6,
    "stealPercent": 2.6,
    "blockPercent": 1.6,
    "turnoverPercent": 14.9,
    "usagePercent": 31.3,
    "offensiveWS": 12.2,
    "defensiveWS": 4.2,
    "winShares": 16.4,
    "winSharesPer": 0.265,
    "offensiveBox": 7,
    "defensiveBox": 1.8,
    "box": 8.8,
    "vorp": 8.1,
    "team": "HOU",
    "season": 2015,
    "playerId": "hardeja01"
  },
  ...
]
```

*(Response truncated for brevity.)*

### 2. Get Advanced Data by Player Name

**GET** `/playerdataadvanced/name/{playerName}`

**Description:**  
Retrieve all advanced data for players whose names match or partially match `playerName`.

### 3. Get Advanced Data by Season

**GET** `/playerdataadvanced/season/{season}`

**Description:**  
Retrieve all advanced data for players in a given season.

### 4. Get Advanced Data by Player ID

**GET** `/playerdataadvanced/playerid/{playerId}`

**Description:**  
Retrieve advanced data by a player's unique or partial `playerId`.

### 5. Get Advanced Data by Team

**GET** `/playerdataadvanced/team/{team}`

**Description:**  
Retrieve advanced data for all players on a given team.

### 6. Count of All Advanced Player Records

**GET** `/playerdataadvanced/count`

**Description:**  
Retrieve the total count of all available advanced player records.

---

## Responses

- **200 OK**: Request successful; returns requested data.
- **404 Not Found**: No matching records found.
- **500 Internal Server Error**: Server encountered an error.

---

## Example Requests

**Query Player Totals (Season 2025, Team BOS):**
```bash
curl -X GET \
  'http://rest.nbaapi.com/api/PlayerDataTotals/query?season=2025&team=BOS&sortBy=PlayerName&ascending=true&pageNumber=1&pageSize=10' \
  -H 'accept: text/plain'
```

**Query Player Advanced (James Harden, Team HOU, Sorted by WinShares Desc):**
```bash
curl -X GET \
  'http://rest.nbaapi.com/api/PlayerDataAdvanced/query?playerName=James%20Harden&team=HOU&sortBy=WinShares&ascending=false&pageNumber=1&pageSize=10' \
  -H 'accept: text/plain'
```

---

## Contact & Support

If you encounter any issues or have questions, please open an issue in this repository or contact me. 😊⛹️🏀🚀

---

You can view the full API documentation at http://rest.nbaapi.com/index.html


