# # import os
# # from dotenv import load_dotenv
# # from binance.client import Client

# # load_dotenv()

# # class BinanceFuturesClient:

# #     def __init__(self):
# #         api_key = os.getenv("BINANCE_API_KEY")
# #         api_secret = os.getenv("BINANCE_API_SECRET")
# #         self.client = Client(api_key, api_secret)
# #         self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
# #         self.client.API_URL = "https://testnet.binancefuture.com"
# #         self.client.TIME_OFFSET = self.client.get_server_time()['serverTime'] - self.client._get_timestamp()

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

        # Binance Futures Testnet URL
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Sync local time with Binance server
        server_time = self.client.get_server_time()
        local_time = int(time.time() * 1000)

        self.client.timestamp_offset = server_time["serverTime"] - local_time