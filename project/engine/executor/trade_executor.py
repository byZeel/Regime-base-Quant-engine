def execute_trades(df):

    # Step 1: Shift signal (next day execution)
    df['position'] = df['signal'].shift(1)

    # Step 2: Daily returns
    df['returns'] = df['close'].pct_change()

    # Step 3: Strategy returns
    df['strategy_returns'] = df['position'] * df['returns']

    # Step 4: Cumulative returns
    df['cum_returns'] = (1 + df['strategy_returns']).cumprod()

    return df