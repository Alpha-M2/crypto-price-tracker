import time
from typing import List

from services.price_service import PriceService, PriceServiceError
from config import DEFAULT_COINS, FETCH_INTERVAL_SECONDS
from logger import setup_logger

logger = setup_logger(__name__)


def display_prices(prices: dict) -> None:
    print("-" * 40)
    for coin, value in prices.items():
        price = value.get("usd")
        print(f"{coin.upper():<15} ${price}")


def run_cli(coins: List[str] = None) -> None:
    coins = coins or DEFAULT_COINS
    service = PriceService()
    logger.info("Starting CLI price tracker")

    while True:
        try:
            prices = service.get_prices(coins)
            display_prices(prices)
        except PriceServiceError as error:
            logger.warning(f"Price fetch failed: {error}")
        time.sleep(FETCH_INTERVAL_SECONDS)
