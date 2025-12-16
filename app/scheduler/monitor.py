import time
from services.price_service import PriceService
from services.alert_service import Alert, AlertService
from services.email_service import EmailService
from config import FETCH_INTERVAL_SECONDS
from logger import setup_logger

logger = setup_logger(__name__)


def start_monitor() -> None:
    logger.info("Starting alert monitor")
    price_service = PriceService()
    alert_service = AlertService()
    email_service = EmailService()

    alerts = [
        Alert(coin="bitcoin", target_price=86381, direction="below"),
        Alert(coin="ethereum", target_price=2800, direction="below"),
        Alert(coin="solana", target_price=120, direction="below"),
        Alert(coin="aster", target_price=0.72, direction="below"),
        Alert(coin="zcash", target_price=400, direction="below"),
    ]

    while True:
        prices = price_service.get_prices([a.coin for a in alerts])
        for alert in alerts:
            current_price = prices[alert.coin]["usd"]
            if alert_service.should_trigger(alert, current_price):
                email_service.send(
                    subject="Crypto Price Alert",
                    body=(
                        f"{alert.coin.upper()} is now ${current_price}\n"
                        f"Target was {alert.direction} ${alert.target_price}"
                    ),
                )
                alert.triggered = True
                logger.info(f"Alert triggered for {alert.coin}")

        time.sleep(FETCH_INTERVAL_SECONDS)
