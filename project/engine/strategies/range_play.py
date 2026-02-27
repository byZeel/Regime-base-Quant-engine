def range_play(df, config):

    support = df['low'].rolling(config['range_window']).min()
    resistance = df['high'].rolling(config['range_window']).max()

    signal = (df['close'] <= support).astype(int)

    return signal