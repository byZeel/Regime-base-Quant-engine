def detect_regime(df, config):
    
    ma = df[f"ma_{config['trend_ma']}"]
    atr = df[f"atr_{config['atr_window']}"]
    
    atr_high = atr.quantile(0.7)
    atr_low = atr.quantile(0.3)
    
    regimes = []
    
    for i in range(len(df)):
        
        if df['close'][i] > ma[i]:
            regimes.append("trend")
            # is price above ma
            # treanding
        elif atr[i] > atr_high:
            regimes.append("volatile")
            # is atr high
            # volatile
        elif atr[i] < atr_low:
            regimes.append("low_vol")
            # is atr low
            # calm
        else:
            regimes.append("range")
            # othrwise
            #side way
    df['regime'] = regimes
    return df