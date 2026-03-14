# import logging
# import os

# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")

# def setup_logging():

#     logging.basicConfig(
#         filename=LOG_FILE,
#         level=logging.INFO,
#         format="%(asctime)s | %(levelname)s | %(message)s"
#     )

#     return logging.getLogger("trading_bot")
import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "trading_bot.log")


def setup_logging():

    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:

        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger