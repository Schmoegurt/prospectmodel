import json
import pandas as pd

with open ('teamids.json') as f:
    teamids = json.load(f)

leagues = []

for league, seasons in teamids.items():
    for season, teams in seasons.items():
        for team, ids in teams.items():
                row = [league, season, team, ids]
                leagues.append(row)


leagues_df = pd.DataFrame(leagues, columns=['league', 'season',
                                            'team', 'team_id'])

leagues_df.to_csv('leagues_hist_table', sep='|', index=False)


