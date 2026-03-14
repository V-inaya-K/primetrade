def validate_side(side):

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):

    order_type = order_type.upper()

    valid = ["MARKET", "LIMIT", "STOP_MARKET"]

    if order_type not in valid:
        raise ValueError(f"Order type must be one of {valid}")

    return order_type


def validate_quantity(qty):

    if qty <= 0:
        raise ValueError("Quantity must be greater than zero")

    return qty


def validate_price(price, order_type):

    if order_type in ["LIMIT", "STOP_MARKET"] and price is None:
        raise ValueError("Price required for LIMIT or STOP_MARKET")

    return price