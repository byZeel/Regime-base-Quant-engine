def trend_strategy(df, config):
    fast = df[f"ma_{config['fast_ma']}"]
    slow = df[f"ma_{config['slow_ma']}"]
    
    signal = (fast > slow).astype(int)
    
    return signal