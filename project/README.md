# Regime-Based Quant Strategy Engine

## 📌 Overview

This project implements a modular trading strategy engine that:

- Detects market regime dynamically
- Selects appropriate strategy based on market conditions
- Executes trades without look-ahead bias
- Tracks performance over time
- Outputs results to Excel

---

## 🧠 System Architecture

The engine works in the following stages:

1. Data Loading
2. Indicator Calculation
3. Regime Detection
4. Strategy Selection
5. Trade Execution
6. Performance Tracking

---

## 📊 Regime Detection

Market regimes are identified using:

| Indicator | Role |
|-----------|------|
| Moving Average | Detect trend |
| ATR | Detect volatility |

Regimes classified:

- Trend
- Volatile
- Low Volatility
- Range

---

## ⚙️ Strategies Implemented

### 1. Trend Following
Uses moving average crossover.

Buy when:

Fast MA > Slow MA

---

### 2. Mean Reversion
Uses RSI.

Buy when:

RSI < 30

---

### 3. Volatility Breakout
Captures momentum using ATR.

Buy when:

Price > Previous High + ATR

---

### 4. Range Play
Uses support levels.

Buy when:

Price near rolling support

---

## 🔄 Strategy Switching

The system dynamically selects strategies:

| Regime | Strategy Used |
|--------|--------------|
| Trend | Trend Following |
| Low Vol | Mean Reversion |
| Volatile | Breakout |
| Range | Range Play |

---

## 🚫 Look-Ahead Bias Prevention

Trades are executed using:

Signal today → Trade tomorrow

Implemented via:

```python
signal.shift(1)
