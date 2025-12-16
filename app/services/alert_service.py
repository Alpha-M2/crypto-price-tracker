from dataclasses import dataclass
from logger import setup_logger

logger = setup_logger(__name__)


@dataclass
class Alert:
    coin: str
    target_price: float
    direction: str
    triggered: bool = False


class AlertService:
    def should_trigger(self, alert: Alert, current_price: float) -> bool:
        if alert.triggered:
            return False
        if alert.direction == "above" and current_price >= alert.target_price:
            return True
        if alert.direction == "below" and current_price <= alert.target_price:
            return True
        return False
