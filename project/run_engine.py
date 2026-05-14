import json
from engine.utils.data_loader import load_data
from engine.utils.indicators import add_ma, add_atr, add_rsi
from engine.regimes.regime_detector import detect_regime
from engine.executor.strategy_switch import apply_strategy
from engine.executor.trade_executor import execute_trades

# Load Config
with open("configs/engine.json") as f:
    config = json.load(f)

# Load Data
df = load_data("data/ohlc_clean.csv")

# Add Indicators
df = add_ma(df, config['trend_ma'])
df = add_ma(df, config['fast_ma'])
df = add_ma(df, config['slow_ma'])

df = add_atr(df, config['atr_window'])
df = add_rsi(df, config['rsi_window'])

# Detect Regime
df = detect_regime(df, config)

# Apply Strategy
df = apply_strategy(df, config)

# Execute Trades
df = execute_trades(df)

# Save Output
df.to_excel("outputs/orders.xlsx", index=False)

print("Engine run complete")