from bot.config import Config
from bot.risk_controls import RiskController
from bot.validation import validate_symbol, validate_trade_amount
from bot.logger import setup_logger


def approve_trade(symbol, amount_usd):
    logger = setup_logger()
    risk = RiskController()

    try:
        Config.validate()

        risk.check_kill_switch()
        validate_symbol(symbol, Config.ALLOWED_SYMBOLS)
        validate_trade_amount(amount_usd, Config.MAX_TRADE_USD)
        risk.check_symbol_allowed(symbol)
        risk.check_trade_size(amount_usd)
        risk.check_daily_loss()

        logger.info(f"TRADE_APPROVED symbol={symbol} amount_usd={amount_usd}")
        return True

    except Exception as error:
        logger.warning(
            f"TRADE_BLOCKED symbol={symbol} amount_usd={amount_usd} reason={error}"
        )
        return False