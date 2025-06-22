import json
import paho.mqtt.client as mqtt
import logging
from paho.mqtt.client import CallbackAPIVersion
from events.publishers.publisher_interface import PublisherInterface
from bop_common.dtos.event_dto import EventDTO
from bop_common.exceptions.publisher_exceptions import (
    PublisherConnectionException,
    PublisherPublishException
)

logger = logging.getLogger(__name__)

class MqttPublisher(PublisherInterface):
    failed_to_connect_error = "Could not connect to MQTT broker =>"
    failed_to_publish_message = "Failed to publish message =>"
    success_publish_message = "Published"

    def __init__(self, host='localhost', port=1883, topic='events'):
        self.log_prefix = f"[🦟 {self.__class__.__name__}]"
        logger.info(f"{self.log_prefix} Attempting to start MQTT Publisher")
        self.host = host
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
        try:
            self.client.connect(self.host, self.port)
            self.client.loop_start()
        except Exception as e:
            raise PublisherConnectionException(f"{self.log_prefix} {self.failed_to_connect_error} {e}")

    def publish(self, message: EventDTO) -> None:
        try:
            payload = json.dumps(message.to_dict())
            result = self.client.publish(self.topic, payload, qos=1)
            if result[0] != mqtt.MQTT_ERR_SUCCESS:
                raise PublisherPublishException(f"{self.log_prefix} {self.failed_to_publish_message}")
        except Exception as e:
            raise PublisherPublishException(f"{self.log_prefix} {self.failed_to_publish_message} {e}")
        logger.info(f"{self.log_prefix} {self.success_publish_message} : {payload}")

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()

    def is_connected(self):
        return self.client.is_connected()