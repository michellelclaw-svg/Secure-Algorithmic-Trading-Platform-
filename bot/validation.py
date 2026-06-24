def validate_symbol(symbol, allowed_symbols):
    if symbol not in allowed_symbols:
        raise ValueError(f"Symbol {symbol} is not allowed.")


def validate_trade_amount(amount, max_trade_usd):
    if amount <= 0:
        raise ValueError("Trade amount must be greater than 0.")
    if amount > max_trade_usd:
        raise ValueError("Trade amount exceeds max allowed trade size.")
