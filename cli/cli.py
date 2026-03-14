import argparse
from bot.orders import OrderService
from bot.validators import *
from bot.logging_config import setup_logging

logger = setup_logging()


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n========= ORDER REQUEST =========")

        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if price:
            print("Price:", price)

        service = OrderService()

        print("\nSending order to Binance Testnet...\n")

        response = service.place_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("========= ORDER RESPONSE =========")

        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\n✅ Order placed successfully")

    except Exception as e:

        print("\n❌ Order failed:", str(e))
        logger.error(str(e))


if __name__ == "__main__":
    main()