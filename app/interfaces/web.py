from flask import Flask, jsonify, render_template_string
from services.price_service import PriceService
from config import DEFAULT_COINS
from logger import setup_logger

logger = setup_logger(__name__)


def start_web_app() -> None:
    app = Flask(__name__)
    price_service = PriceService()

    @app.route("/")
    def index():
        try:
            prices = price_service.get_prices(DEFAULT_COINS)
            return render_template_string(_html_template(), prices=prices)
        except Exception:
            logger.error("Failed to load prices", exc_info=True)
            return "Service unavailable", 503

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    logger.info("Starting web interface")
    app.run(debug=True)


def _html_template() -> str:
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Crypto Price Tracker</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 2rem; }
            table { border-collapse: collapse; }
            th, td { padding: 0.5rem 1rem; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <h2>Live Crypto Prices</h2>
        <table>
            <tr>
                <th>Coin</th>
                <th>Price (USD)</th>
            </tr>
            {% for coin, value in prices.items() %}
            <tr>
                <td>{{ coin.upper() }}</td>
                <td>${{ value.usd }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
