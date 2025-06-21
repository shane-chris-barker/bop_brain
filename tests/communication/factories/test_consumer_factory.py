import unittest
from unittest.mock import MagicMock, patch
from communication.factories.consumer_factory import get_consumer
from communication.consumers.mqtt_consumer import MqttConsumer

class TestCommunicationFactory(unittest.TestCase):
    patch_config = "communication.factories.consumer_factory.get_config"

    @patch(patch_config)
    def test_get_consumer_returns_mqtt_consumer(self, mock_get_config):
        mock_config = MagicMock()
        mock_config.COMM_TYPE = 'mqtt'
        mock_config.MQTT_HOST = 'localhost'
        mock_config.MQTT_PORT = '1883'
        mock_config.INPUT_COMM_NAME = 'communications'
        mock_get_config.return_value = mock_config
        consumer = get_consumer()
        assert isinstance(consumer, MqttConsumer)
        assert consumer.host == mock_config.MQTT_HOST
        assert consumer.port == mock_config.MQTT_PORT
        assert consumer.topic == mock_config.INPUT_COMM_NAME

    @patch(patch_config)
    def test_get_consumer_fallback_exception(self, mock_get_config):
        mock_config = MagicMock()
        mock_config.COMM_TYPE = 'unsupported'
        mock_get_config.return_value = mock_config

        with self.assertLogs(level='WARNING') as log:
            consumer = get_consumer()
            self.assertIsNone(consumer)
            self.assertTrue(any("Warning: Cannot boot Consumer" in message for message in log.output))
