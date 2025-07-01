# NBA Stats API 2.0

## 🔎 View the Interactive API Documentation
**[Interactive Swagger Documentation](https://api.server.nbaapi.com/swagger/index.html)** - Complete API reference with live testing capabilities

## Introduction

This documentation provides comprehensive information for using the NBA Stats API. The API offers access to NBA season and playoff statistics, including player totals, advanced metrics, and historical data. All statistics are cross-referenced with [basketball-reference.com](https://www.basketball-reference.com/) and [NBA.com](https://www.nba.com/stats).

# NBA Player Statistics API

This API provides endpoints to query NBA player statistics, including both "Totals" data and "Advanced" statistical data. Each endpoint supports filtering, sorting, and pagination options to help you retrieve exactly the data you need.

## Base URL

All API endpoints are served from:

```
https://api.server.nbaapi.com/
```

## Authentication

No authentication is currently required for these endpoints.

## Available Endpoints

- **Player Advanced Stats** (`/api/playeradvancedstats`)
  
  Provides advanced player metrics including Player Efficiency Rating (PER), True Shooting Percentage (TS%), Usage Percentage, Win Shares, VORP, and other advanced analytics.

- **Player Totals** (`/api/playertotals`)

  Provides season-based totals such as points, assists, rebounds, games played, shooting percentages, and more traditional statistics.

---

## Common Query Parameters

Both endpoints support the following query parameters:

### Filtering Parameters
- **season** *(integer, optional)*: Filter by a specific season (e.g., `2025`)
- **team** *(string, optional)*: Filter by team abbreviation (e.g., `MIL`, `LAL`)
- **playerId** *(string, optional)*: Filter by player's unique ID (e.g., `greenaj01`)
- **isPlayoff** *(boolean, optional)*: Filter for playoff statistics (`true`) or regular season (`false`)

### Pagination Parameters
- **page** *(integer, optional)*: Page number to retrieve (default: `1`)
- **pageSize** *(integer, optional)*: Number of records per page (default: `20`)

### Sorting Parameters
- **sortBy** *(string, optional)*: Field name to sort results by (see endpoint-specific options below)
- **ascending** *(boolean, optional)*: Sort order - `true` for ascending, `false` for descending (default: `false`)

---

## Player Advanced Stats Endpoint

**GET** `/api/playeradvancedstats`

Retrieve advanced player statistics with comprehensive filtering and sorting options.

### Sorting Options for Advanced Stats

The `sortBy` parameter accepts the following values:
- `games` - Games played
- `minutes_played` - Total minutes played
- `ts_percent` - True Shooting Percentage
- `total_rb_percent` - Total Rebound Percentage
- `usage_percent` - Usage Percentage
- `offensive_ws` - Offensive Win Shares
- `defensive_ws` - Defensive Win Shares
- `win_shares` - Total Win Shares (default)
- `win_shares_per` - Win Shares per 48 minutes
- `offensive_box` - Offensive Box Plus/Minus
- `defensive_box` - Defensive Box Plus/Minus
- `box` - Total Box Plus/Minus
- `vorp` - Value Over Replacement Player
- `season` - Season year

### Example Request

```bash
curl -X GET \
  'https://api.server.nbaapi.com/api/playeradvancedstats?page=1&pageSize=20&sortBy=win_shares&ascending=false&season=2025&team=MIL' \
  -H 'accept: application/json'
```

### Response Format

```json
{
  "data": [
    {
      "id": 12345,
      "playerName": "Giannis Antetokounmpo",
      "position": "PF",
      "age": 30,
      "games": 65,
      "minutesPlayed": 2205,
      "per": 31.2,
      "tsPercent": 0.614,
      "threePAR": 0.156,
      "ftr": 0.345,
      "offensiveRBPercent": 11.2,
      "defensiveRBPercent": 34.5,
      "totalRBPercent": 22.8,
      "assistPercent": 40.1,
      "stealPercent": 1.8,
      "blockPercent": 3.2,
      "turnoverPercent": 16.7,
      "usagePercent": 36.8,
      "offensiveWS": 12.3,
      "defensiveWS": 4.7,
      "winShares": 17.0,
      "winSharesPer": 0.370,
      "offensiveBox": 8.9,
      "defensiveBox": 2.1,
      "box": 11.0,
      "vorp": 9.2,
      "team": "MIL",
      "season": 2025,
      "playerId": "antetgi01",
      "isPlayoff": false
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 450,
    "pages": 23
  }
}
```

---

## Player Totals Endpoint

**GET** `/api/playertotals`

Retrieve traditional player statistics including points, assists, rebounds, and shooting data.

### Sorting Options for Player Totals

The `sortBy` parameter accepts the following values:
- `games` - Games played
- `minutes_pg` - Minutes per game
- `three_fg` - Three-point field goals made
- `three_attempts` - Three-point field goal attempts
- `two_fg` - Two-point field goals made
- `effect_fg_percent` - Effective Field Goal Percentage
- `ft` - Free throws made
- `total_rb` - Total rebounds
- `assists` - Assists
- `steals` - Steals
- `blocks` - Blocks
- `points` - Points scored
- `season` - Season year

### Example Request

```bash
curl -X GET \
  'https://api.server.nbaapi.com/api/playertotals?page=1&pageSize=20&sortBy=points&ascending=false&season=2025' \
  -H 'accept: application/json'
```

### Response Format

```json
{
  "data": [
    {
      "id": 67890,
      "playerName": "Luka Doncic",
      "position": "PG",
      "age": 26,
      "games": 70,
      "gamesStarted": 70,
      "minutesPg": 36.2,
      "fieldGoals": 11.2,
      "fieldAttempts": 23.1,
      "fieldPercent": 0.485,
      "threeFg": 4.1,
      "threeAttempts": 11.3,
      "threePercent": 0.363,
      "twoFg": 7.1,
      "twoAttempts": 11.8,
      "twoPercent": 0.602,
      "effectFgPercent": 0.574,
      "ft": 7.8,
      "ftAttempts": 9.2,
      "ftPercent": 0.848,
      "offensiveRb": 1.8,
      "defensiveRb": 7.4,
      "totalRb": 9.2,
      "assists": 8.9,
      "steals": 1.4,
      "blocks": 0.5,
      "turnovers": 4.1,
      "personalFouls": 2.8,
      "points": 34.3,
      "team": "DAL",
      "season": 2025,
      "playerId": "doncilu01",
      "isPlayoff": false
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "total": 500,
    "pages": 25
  }
}
```

---

## Response Codes

- **200 OK**: Request successful; returns requested data
- **400 Bad Request**: Invalid query parameters
- **404 Not Found**: No matching records found
- **500 Internal Server Error**: Server encountered an error

---

## Usage Examples

### Get Top Win Shares Leaders (Advanced Stats)

```bash
curl -X GET \
  'https://api.server.nbaapi.com/api/playeradvancedstats?page=1&pageSize=10&sortBy=win_shares&ascending=false&season=2025' \
  -H 'accept: application/json'
```

### Get Leading Scorers (Player Totals)

```bash
curl -X GET \
  'https://api.server.nbaapi.com/api/playertotals?page=1&pageSize=10&sortBy=points&ascending=false&season=2025' \
  -H 'accept: application/json'
```

### Get Boston Celtics Players Advanced Stats

```bash
curl -X GET \
  'https://api.server.nbaapi.com/api/playeradvancedstats?team=BOS&season=2025&page=1&pageSize=20&sortBy=vorp&ascending=false' \
  -H 'accept: application/json'
```

### Get Playoff Statistics

```bash
curl -X GET \
  'https://api.server.nbaapi.com/api/playertotals?isPlayoff=true&season=2024&sortBy=points&ascending=false' \
  -H 'accept: application/json'
```

---

## Additional Resources

- **Interactive Documentation**: [https://api.server.nbaapi.com](https://api.server.nbaapi.com/swagger/index.html)
- **Postman Collection**: Use the "Run in Postman" button above
- **Data Sources**: Statistics cross-referenced with Basketball Reference and NBA.com

---

## Contact & Support

If you encounter any issues or have questions about the API, please open an issue in the repository or contact the development team. 🏀🚀

---

**Note**: This API is currently in public beta. Features and endpoints may be updated based on user feedback and requirements.
