import os
from dotenv import load_dotenv

load_dotenv()

# Binance Configuration
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET')
TRADING_PAIR = os.getenv('TRADING_PAIR', 'XAUUSDT')

# Telegram Configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Trading Parameters
TIMEFRAMES = os.getenv('TIMEFRAMES', '5m,15m,1h').split(',')
TAKE_PROFIT_PERCENT = float(os.getenv('TAKE_PROFIT_PERCENT', 3))
STOP_LOSS_PERCENT = float(os.getenv('STOP_LOSS_PERCENT', 2))
RISK_PER_TRADE = float(os.getenv('RISK_PER_TRADE', 0.02))

# Technical Indicators Thresholds
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70
RSI_PERIOD = 14

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

ATR_PERIOD = 14

# News Configuration
NEWS_API_KEY = os.getenv('NEWS_API_KEY', '')
CHECK_NEWS_INTERVAL = int(os.getenv('CHECK_NEWS_INTERVAL', 3600))

# Alert Settings
CONSOLE_ALERTS = True
TELEGRAM_ALERTS = True
LOG_TRADES = True

# Retry Settings
MAX_RETRIES = 3
RETRY_DELAY = 5
