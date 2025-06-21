import logging
logger = logging.getLogger(__name__)
import json
import paho.mqtt.client as mqtt
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.consumers.consumer_interface import ConsumerInterface

class MqttConsumer(ConsumerInterface):

    def __init__(
            self,
            host: str = 'localhost',
            port: int = 1883,
            topic: str = 'communications'
    ):
        self.host = host
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.log_prefix = f"[🦟 MQTT Consumer]"
        self._is_connected = False

    def consume(self, message: CommunicationDTO) -> None:
        logger.info(f"{self.log_prefix} consumed message {message}")

    def _on_connect(self, client, userdata, flags, reason_code, properties=None):
        if reason_code  == 0:
            logger.info(f"{self.log_prefix} Connected to broker")
            self._is_connected = True
            client.subscribe(self.topic)
        else:
            self._is_connected = False
            logger.info(f"{self.log_prefix} Connection failed")

    def _on_message(self, client, userdata, message):
        payload = message.payload.decode("utf-8")

        try:
            data = json.loads(payload)
            message = CommunicationDTO(**data)
            self.consume(message)
        except Exception as e:
            logger.error(f"{self.log_prefix} {e}")

    def start(self) -> None:
        logger.info(f"{self.log_prefix} Starting MQTT Consumer")
        self.client.connect(self.host, self.port, 60)
        self.client.loop_start()

    def stop(self) -> None:
        logger.info(f"{self.log_prefix} Stopping MQTT Consumer")
        self.client.loop_stop()
        self.client.disconnect()
