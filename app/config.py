import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "development")

COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
DEFAULT_CURRENCY = "usd"
DEFAULT_COINS = ["bitcoin", "ethereum", "solana", "aster", "zcash"]

REQUEST_TIMEOUT = 10  # in seconds
FETCH_INTERVAL_SECONDS = 15

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
