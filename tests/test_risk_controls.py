import pytest
from bot.risk_controls import RiskController
from bot.config import Config


def test_kill_switch_blocks_when_enabled(monkeypatch):
    monkeypatch.setattr(Config, "KILL_SWITCH", True)
    risk = RiskController()

    with pytest.raises(Exception):
        risk.check_kill_switch()


def test_symbol_allowed_accepts_valid_symbol(monkeypatch):
    monkeypatch.setattr(Config, "ALLOWED_SYMBOLS", ["BTCUSDT", "ETHUSDT"])
    risk = RiskController()
    risk.check_symbol_allowed("BTCUSDT")


def test_symbol_allowed_blocks_invalid_symbol(monkeypatch):
    monkeypatch.setattr(Config, "ALLOWED_SYMBOLS", ["BTCUSDT", "ETHUSDT"])
    risk = RiskController()

    with pytest.raises(Exception):
        risk.check_symbol_allowed("DOGEUSDT")


def test_trade_size_blocks_large_amount(monkeypatch):
    monkeypatch.setattr(Config, "MAX_TRADE_USD", 100)
    risk = RiskController()

    with pytest.raises(Exception):
        risk.check_trade_size(150)


def test_daily_loss_blocks_when_limit_reached(monkeypatch):
    monkeypatch.setattr(Config, "MAX_DAILY_LOSS_USD", 50)
    risk = RiskController()
    risk.daily_loss = 50

    with pytest.raises(Exception):
        risk.check_daily_loss()
