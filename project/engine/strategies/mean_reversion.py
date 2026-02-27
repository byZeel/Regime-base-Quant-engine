def mean_reversion(df):

    signal = (df['rsi'] < 30).astype(int)

    return signal