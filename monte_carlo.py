import pandas as pd

premier_league_teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Leeds United",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sunderland",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers"
]

table = pd.DataFrame(dict(team = premier_league_teams, games = [0] * len(premier_league_teams),points = [0] * len(premier_league_teams)))

print(table)


# basic simulation
import random

table = table0.copy()

n_sims = 50

for i in range(n_sims):
  for home in premier_league_teams:
      for away in premier_league_teams:
        if home != away:
          result = random.random()
          # MVP: assume 50% chance for any home team
          if result > 0.5:
            table.loc[table.team == home, "points"] += 3
          # MVP: assume 20% chance for any away team
          elif result > 0.7:
            table.loc[table.team == away, "points"] += 3
          # MVP: assume 30% chance for a draw
          else:
            table.loc[table.team == home, "points"] += 1
            table.loc[table.team == away, "points"] += 1
          
          table.loc[table.team == home, "games"] += 1
          table.loc[table.team == away, "games"] += 1

# final EPL table
table['points'] = table['points'].div(n_sims)
table['games'] = table['games'].div(n_sims)

table = table.sort_values(by = "points", ascending = False)
table.index = range(1, len(table) + 1)
print(table)
