from bot.config import Config
from bot.logger import setup_logger
from bot.risk_controls import RiskController
from bot.validation import validate_symbol, validate_trade_amount


def main():
    Config.validate()
    logger = setup_logger()
    risk = RiskController()

    symbol = "BTCUSDT"
    amount = 50

    try:
        risk.check_kill_switch()
        validate_symbol(symbol, Config.ALLOWED_SYMBOLS)
        validate_trade_amount(amount, Config.MAX_TRADE_USD)
        risk.check_symbol_allowed(symbol)
        risk.check_trade_size(amount)
        risk.check_daily_loss()

        logger.info(f"Trade approved: {symbol} for ${amount}")
        print("Trade approved.")

    except Exception as error:
        logger.error(f"Trade blocked: {error}")
        print(f"Trade blocked: {error}")


if __name__ == "__main__":
    main()
