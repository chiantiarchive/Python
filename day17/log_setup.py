import logging
from logging.handlers import RotatingFileHandler


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler("app.log", maxBytes=1_000_000,
                                 backupCount=3, encoding="utf-8"),
            logging.StreamHandler(),
        ]
    )