# 🧠 F&O Alert Bot (Fully Automated with Telegram Alerts)

This is a fully automated F&O (Futures and Options) alert bot that analyzes NIFTY movements and sends trade signals to a Telegram channel based on various technical indicators.

## ✅ Features

- 📊 EMA 9/15 crossover detection
- 📈 RSI and MACD indicator filtering
- 🧠 Smart Money Concepts (support/resistance zones, liquidity grabs, BOS)
- 🧪 Backtesting logic included with logs (`backtest_log.csv`)
- 🕒 Multi-timeframe analysis
- 🛡️ Risk-managed Stop Loss based on ₹10,000 capital
- 📤 Sends alerts via Telegram
- 🔄 Runs every 5 minutes (during market hours)
- 🌐 Flask server included for UptimeRobot monitoring
- ☁️ Works on Replit, Termux, or any local system

## 📦 Files

- `main.py` - Main bot runner with scheduler
- `signal_generator.py` - Logic for generating trade signals
- `telegram_bot.py` - Sends messages to Telegram
- `utils.py` - Helpers for market hours and SMC zones
- `server.py` - Flask app for uptime monitoring
- `backtest_log.csv` - Strategy log file
- `.env` - Add your secret `BOT_TOKEN` here (not committed)

## 🧪 Backtesting

Log file `backtest_log.csv` tracks:
- Trade side (BUY/SELL)
- SL/Target hit
- PnL
- Total wins/losses

## 🚀 Setup Instructions

1. **Add your bot token**  
Create `.env` file with this content:
```bash
BOT_TOKEN=your_bot_token_here
```

2. **Install requirements**
```bash
pip install -r requirements.txt
```

3. **Run the bot**
```bash
python main.py
```

## 🌍 Deploy on Replit or Termux

1. Upload the folder
2. Add secret `BOT_TOKEN` via Replit UI
3. Set Flask uptime monitor endpoint (`server.py`)
4. Add UptimeRobot ping URL

## 🧠 Strategy Logic

Trade signals are generated only when **all of the following** are aligned:
- EMA 9 crosses EMA 15
- RSI in valid overbought/oversold zone
- MACD crossover aligns with trend
- Price respects support/resistance zones
- Multi-timeframe confirmation (5m, 15m, 1hr)

---

### 📈 Built by [abeed93](https://github.com/abeed93)
