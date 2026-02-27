#MA
def add_ma(df,window):
    df[f"ma_{window}"] = df['close'].rolling(window).mean()
    return df

# Takes average of last N prices.
# Example
# If window = 50
# 50-day trend line
# Used for
# Trend detection.

#ATR
def add_atr(df, window):
    df['tr'] = df[['high','low','close']].apply(
        lambda row: max(
            row['high'] - row['low'],
            abs(row['high'] - row['close']),
            abs(row['low'] - row['close'])
        ), axis=1
    )
    
    df[f"atr_{window}"] = df['tr'].rolling(window).mean()
    return df

# Measures
# Movement size
# High ATR = volatile
# Low ATR = calm

#RSI
def add_rsi(df, window):
    
    delta = df['close'].diff()
    
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    
    rs = avg_gain / avg_loss
    
    df['rsi'] = 100 - (100 / (1 + rs))
    
    return df

# Measures:
# Overbought / Oversold
# Mean reversion strategy.
# RSI < 30 → oversold → buy
# RSI > 70 → overbought → sell