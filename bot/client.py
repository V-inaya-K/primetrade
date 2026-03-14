from binance.client import Client
import os
import time
from dotenv import load_dotenv

load_dotenv()


class BinanceFuturesClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(api_key, api_secret)

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        server_time = self.client.get_server_time()#to sync with local time
        local_time = int(time.time() * 1000)#calculate local time in milliseconds
        self.client.timestamp_offset = server_time["serverTime"] - local_time