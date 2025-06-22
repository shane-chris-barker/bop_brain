import logging
from events.publishers.amqp_publisher import AmqpPublisher
from events.publishers.mock_publisher import MockPublisher
from events.publishers.mqtt_publisher import MqttPublisher
from config import get_config

logger = logging.getLogger(__name__)

def get_publisher():
    config = get_config()
    log_prefix = "[📢 PUBLISHER FACTORY]"
    logger.info(f"{log_prefix} is trying to start the {config.COMM_TYPE} Publisher...")
    try:
        if config.COMM_TYPE == 'mqtt':
            publisher = MqttPublisher(
                host=config.MQTT_HOST,
                port=config.MQTT_PORT,
                topic=config.OUTPUT_COMM_NAME
            )
            logger.info(f"{log_prefix} 🦟 MQTT Publisher created successfully")
            return publisher
        elif config.COMM_TYPE == 'amqp':
            publisher = AmqpPublisher(
                host=config.AMQP_HOST,
                port=config.AMQP_PORT,
                queue_name=config.OUTPUT_COMM_NAME
            )
            logger.info(f"{log_prefix} 🐇 AMQP Publisher created successfully")
            return publisher
        elif config.COMM_TYPE == 'mock':
            publisher = MockPublisher()
            logger.info(f"{log_prefix} 🥷 Mock Publisher created successfully")
            return publisher
        else:
            raise ValueError(f"{log_prefix} Unsupported Publisher Type")
    except Exception as e:
        logger.warning(f"{log_prefix} Warning: Cannot boot Publisher - Falling back to mock because of {e}")
        return MockPublisher()