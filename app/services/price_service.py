import requests
from typing import Dict, List

from config import COINGECKO_BASE_URL, DEFAULT_CURRENCY, REQUEST_TIMEOUT

from logger import setup_logger

logger = setup_logger(__name__)


class PriceServiceError(Exception):
    """Raised when price fetching fails."""


class PriceService:
    def get_prices(self, coin_ids: List[str]) -> Dict[str, Dict[str, float]]:
        try:
            response = requests.get(
                COINGECKO_BASE_URL,
                params={
                    "ids": ",".join(coin_ids),
                    "vs_currencies": DEFAULT_CURRENCY,
                },
            )
            response.raise_for_status()
            data = response.json()

            if not data:
                raise PriceServiceError("Empty response from price API")

            return data
        except requests.RequestException as exc:
            logger.error("Failed to fetch prices", exc_info=True)
            raise PriceServiceError(str(exc)) from exc
