from bot.config import Config


class RiskController:
    def __init__(self):
        self.daily_loss = 0

    def check_kill_switch(self):
        if Config.KILL_SWITCH:
            raise Exception("Trading halted: kill switch is enabled.")

    def check_symbol_allowed(self, symbol):
        if symbol not in Config.ALLOWED_SYMBOLS:
            raise Exception(f"Trading blocked: {symbol} is not approved.")

    def check_trade_size(self, usd_amount):
        if usd_amount > Config.MAX_TRADE_USD:
            raise Exception("Trading blocked: trade size exceeds limit.")

    def check_daily_loss(self):
        if self.daily_loss >= Config.MAX_DAILY_LOSS_USD:
            raise Exception("Trading blocked: daily loss limit reached.")
