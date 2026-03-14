import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from bot.orders import OrderService
from bot.logging_config import setup_logging

logger = setup_logging()

st.title("Binance Futures Testnet Trading Bot")

symbol = st.text_input("Symbol", "BTCUSDT")

side = st.selectbox("Side", ["BUY", "SELL"])

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT", "STOP_MARKET"]
)

quantity = st.number_input("Quantity", min_value=0.0)

price = None

if order_type in ["LIMIT", "STOP_MARKET"]:
    price = st.number_input("Price")

if st.button("Place Order"):

    service = OrderService()

    response = service.place_order(
        symbol,
        side,
        order_type,
        quantity,
        price
    )

    st.success("Order placed!")

    st.json(response)