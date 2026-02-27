from engine.strategies.trend_strategy import trend_strategy
from engine.strategies.mean_reversion import mean_reversion
from engine.strategies.volatility_breakout import volatility_breakout
from engine.strategies.range_play import range_play

def apply_strategy(df, config):

    trend_sig = trend_strategy(df, config)
    mean_sig = mean_reversion(df)
    vol_sig = volatility_breakout(df, config)
    range_sig = range_play(df, config)

    signals = []

    for i in range(len(df)):

        regime = df['regime'][i]

        if regime == "trend":
            signals.append(trend_sig[i])

        elif regime == "low_vol":
            signals.append(mean_sig[i])

        elif regime == "volatile":
            signals.append(vol_sig[i])

        elif regime == "range":
            signals.append(range_sig[i])

        else:
            signals.append(0)

    df['signal'] = signals

    return df