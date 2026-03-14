import logging
from .client import BinanceFuturesClient

logger = logging.getLogger("trading_bot")


class OrderService:

    def __init__(self):
        self.client = BinanceFuturesClient().client


    def place_market_order(self, symbol, side, quantity):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
            recvWindow=10000
        )


    def place_limit_order(self, symbol, side, quantity, price):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
            recvWindow=10000
        )


    def place_stop_market_order(self, symbol, side, quantity, stop_price):

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=stop_price,
            quantity=quantity,
            recvWindow=10000
        )


    def place_order(self, symbol, side, order_type, quantity, price=None):

        logger.info(
            f"Order request {symbol} {side} {order_type} qty={quantity} price={price}"
        )

        try:

            if order_type == "MARKET":
                response = self.place_market_order(symbol, side, quantity)

            elif order_type == "LIMIT":
                response = self.place_limit_order(symbol, side, quantity, price)

            elif order_type == "STOP_MARKET":
                response = self.place_stop_market_order(symbol, side, quantity, price)

            else:
                raise ValueError("Unsupported order type")

            logger.info(f"Order response {response}")

            return response

        except Exception as e:

            logger.error(f"Order failed {str(e)}")
            raise