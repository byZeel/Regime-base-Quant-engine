def volatility_breakout(df, config):

    atr = df[f"atr_{config['atr_window']}"]
    prev_high = df['high'].shift(1)

    signal = (df['close'] > prev_high + atr).astype(int)

    return signal