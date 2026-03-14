# Binance Futures Testnet Trading Bot Task💻

## Setup

1. Clone repo

2. Install dependencies using command: pip install -r requirements.txt

3. Create .env file and add your API credentials.

4. Run CLI, for market order, limit order and stop market order respectively

  python -m cli.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001<br>
  python -m cli.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000<br>
  python -m cli.cli --symbol BTCUSDT --side BUY --type STOP_MARKET --quantity 0.001 --price 65000

5. Run UI

streamlit run ui/app.py

## Features

- Buy Market orders
- Limit sell orders
- Stop Market buy orders
- CLI interface availablity
- Streamlit UI availablity
- Logging of orders
- Error handling