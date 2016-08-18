# solutions_tidy.py

# Step 1
id_vars = ['game_id', 'date', 'home_win']
value_vars = ['home_team', 'away_team']
value_name = 'team'
var_name = 'home_or_away'

games = pd.melt(df.reset_index(),
                id_vars=id_vars,
                value_name=value_name, var_name=var_name,
                value_vars=value_vars)
games.head()

# Step 2
games['win'] = games.home_win == (games.home_or_away == 'home_team')
games.head()

# Step 3
wins = (games.groupby(['team', 'home_or_away']).win
             .agg({"n_wins": "sum",
                   "n_games": "count",
                   "win_pct": "mean"}))
wins.head()

# Step 4
win_percent = (
    # Use sum(wins) / sum(games) since I don't
    # know if teams play the same number of games at
    # home as away
    wins.groupby(level='team', as_index=True)
    .apply(lambda x: x.n_wins.sum() / x.n_games.sum())
)
win_percent.head()

# Step 5
df = df.assign(away_strength=df['away_team'].map(win_percent),
               home_strength=df['home_team'].map(win_percent),
               point_diff=df['home_points'] - df['away_points'],
               rest_diff=df['home_rest'] - df['away_rest'])
df['home_win'] = df.home_win.astype(int)
df.head()
