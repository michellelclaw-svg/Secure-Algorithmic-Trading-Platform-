import pytest
from bot.validation import validate_symbol, validate_trade_amount


def test_validate_symbol_allows_valid_symbol():
    validate_symbol("BTCUSDT", ["BTCUSDT", "ETHUSDT"])


def test_validate_symbol_blocks_invalid_symbol():
    with pytest.raises(ValueError):
        validate_symbol("DOGEUSDT", ["BTCUSDT", "ETHUSDT"])


def test_validate_trade_amount_allows_valid_amount():
    validate_trade_amount(50, 100)


def test_validate_trade_amount_blocks_zero_or_negative():
    with pytest.raises(ValueError):
        validate_trade_amount(0, 100)

    with pytest.raises(ValueError):
        validate_trade_amount(-10, 100)


def test_validate_trade_amount_blocks_amount_above_limit():
    with pytest.raises(ValueError):
        validate_trade_amount(150, 100)
