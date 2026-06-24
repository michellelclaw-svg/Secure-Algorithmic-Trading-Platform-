import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    API_KEY = os.getenv("EXCHANGE_API_KEY")
    API_SECRET = os.getenv("EXCHANGE_API_SECRET")
    MAX_TRADE_USD = float(os.getenv("MAX_TRADE_USD", "100"))
    MAX_DAILY_LOSS_USD = float(os.getenv("MAX_DAILY_LOSS_USD", "50"))
    ALLOWED_SYMBOLS = os.getenv("ALLOWED_SYMBOLS", "BTCUSDT,ETHUSDT").split(",")
    KILL_SWITCH = os.getenv("KILL_SWITCH", "false").lower() == "true"

    @classmethod
    def validate(cls):
        if not cls.API_KEY or not cls.API_SECRET:
            raise ValueError("Missing API credentials.")
