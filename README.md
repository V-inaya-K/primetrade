# Binance Testnet Trading Bot Task 💻

## Setup

1. Clone repo

2. Install dependencies using command:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in root directory and add your API credentials.

5. Run CLI, for market order, limit order and stop market order as per requirement.

5. Run Streamlit UI.

## Examples

### Example 1 — Market Order

```bash
python -m cli.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Example 2 — Limit Order

```bash
python -m cli.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

### Example 3 — Stop Market Order

```bash
python -m cli.cli --symbol BTCUSDT --side BUY --type STOP_MARKET --quantity 0.001 --price 65000
```

### Example 4 — Using the UI

```bash
streamlit run ui/app.py
```

Then open the browser:

```
http://localhost:8501
```

Use the UI form to place orders.

---

## Features

- Buy Market orders
- Limit sell orders
- Stop Market buy orders
- CLI interface availability
- Streamlit UI availability
- Logging of orders
- Error handling

## Problems Faced

- **Local time mismatch with Binance server** which caused  
  `APIError(code=-1021): Timestamp for this request was ahead of server time`.

- This was resolved by synchronizing the system time and implementing a **timestamp offset calculation using Binance server time** inside the client initialization.

- Minor module import issues due to project structure were resolved by ensuring proper package initialization (`__init__.py`) and correct file naming.
