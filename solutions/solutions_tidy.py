# Final

def win_pct_step_1(df):
    wins = pd.melt(df.reset_index(),
                   id_vars=['game_id', 'date', 'home_win'],
                   value_name='team', var_name='home_or_away',
                   value_vars=['home_team', 'away_team'])
    return wins


def win_pct_step_2(wins):
    return wins.assign(win=lambda x: x.home_win == (x.home_or_away == 'home_team'))


def win_pct_step_3(wins):
    aggregated = (wins.groupby(['team', 'home_or_away']).win
                      .agg({"n_wins": "sum",
                            "n_games": "count",
                            "win_pct": "mean"}))
    return aggregated


def win_pct(df):
    wins = (
        pd.melt(df.reset_index(),
                id_vars=['game_id', 'date', 'home_win'],
                value_name='team', var_name='home_or_away',
                value_vars=['home_team', 'away_team'])
       .assign(win=lambda x: x.home_win == (x.home_or_away == 'home_team'))
       .groupby(['team', 'home_or_away'])
       .win
       .agg({'n_wins': 'sum', 'n_games': 'count', 'win_pct': 'mean'})
    )
    return wins


def win_percent(wins):
    aggregated = (
    # Use sum(wins) / sum(games) since I don't
    # know if teams play the same number of games at
    # home as away
        wins.groupby(level='team', as_index=True)
            .apply(lambda x: x.n_wins.sum() / x.n_games.sum())
    )
    return win_percent
