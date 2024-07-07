from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

def test_incrementer(num: int) -> int:
    logger.info(f"Incrementing {num}")
    num = num + 1
    return num