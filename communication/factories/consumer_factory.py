import logging
logger = logging.getLogger(__name__)
from config import get_config
from communication.consumers.mqtt_consumer import MqttConsumer

def get_consumer():
    config = get_config()
    log_prefix = "[📢 CONSUMER FACTORY]"
    logger.info(f"{log_prefix} is trying to start the {config.COMM_TYPE} consumer...")
    try:
        if config.COMM_TYPE == 'mqtt':
            consumer = MqttConsumer(
                host=config.MQTT_HOST,
                port=config.MQTT_PORT,
                topic=config.INPUT_COMM_NAME
            )
            logger.info(f"{log_prefix} 🦟 MQTT Consumer created successfully")
            return consumer
        else:
            raise ValueError(f"{log_prefix} Unsupported Publisher Type")
    except Exception as e:
        logger.warning(f"{log_prefix} Warning: Cannot boot Consumer - {e}")
