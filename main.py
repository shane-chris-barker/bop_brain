from logger_config import setup_logging
import logging
setup_logging()

from communication.factories.consumer_factory import get_consumer
from communication.handlers.registry_setup import register_handlers
import time
logger = logging.getLogger(__name__)

def main():
    log_prefix = "[🤖 MAIN]"
    logger.info(f"{log_prefix} Bop Brain is waking up")
    register_handlers()
    consumer = get_consumer()
    consumer.start()
    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        logger.info(f"{log_prefix} Bop Brain Is Shutting down")
    finally:
        consumer.stop()

if __name__ == "__main__":
    main()
