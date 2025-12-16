import smtplib
from email.message import EmailMessage

from config import (
    SMTP_SERVER,
    SMTP_PORT,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECEIVER,
)
from logger import setup_logger

logger = setup_logger(__name__)


class EmailService:
    def send(self, subject: str, body: str) -> None:
        if not all([EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER]):
            logger.warning("Email credentials not configured")
            return

        try:
            message = EmailMessage()
            message["From"] = EMAIL_SENDER
            message["To"] = EMAIL_RECEIVER
            message["Subject"] = subject
            message.set_content(body)

            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
                server.login(EMAIL_SENDER, EMAIL_PASSWORD)
                server.send_message(message)

            logger.info("Alert email sent")

        except smtplib.SMTPException as exc:
            logger.error("Failed to send alert email", exc_info=True)
