import json
from unittest.mock import MagicMock
from communication.consumers.mqtt_consumer import MqttConsumer
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.hardware_type import HardwareType
class TestMqttConsumer:

    def test_on_connect_sets_flag_and_subscribes(self):
        consumer = MqttConsumer()
        mock_client = MagicMock()
        consumer._on_connect(mock_client, None, None, reason_code=0)
        assert consumer._is_connected is True
        mock_client.subscribe.assert_called_once_with(consumer.topic)

    def test_on_connect_failure_sets_flag(self):
        consumer = MqttConsumer()
        mock_client = MagicMock()
        consumer._on_connect(mock_client, None, None, reason_code=1)
        assert consumer._is_connected is False
        mock_client.subscribe.assert_not_called()

    def test_on_message_valid_payload_triggers_consume(self):
        consumer = MqttConsumer()
        data = {"input":HardwareType.TEST_HARDWARE.value, "content": {"text": "hello"}}
        mock_message = MagicMock()
        mock_message.payload = json.dumps(data).encode("utf-8")

        consumer.consume = MagicMock()
        consumer._on_message(None, None, mock_message)
        consumer.consume.assert_called_once()
        called_message = consumer.consume.call_args[0][0]
        assert isinstance(called_message, CommunicationDTO)

    def test_on_invalid_payload(self, caplog):
        consumer = MqttConsumer()
        mock_message = MagicMock()
        mock_message.payload = b"hello, I am not valid Json"
        consumer._on_message(None, None, mock_message)
        assert any("[🦟 MQTT Consumer]" in rec.message for rec in caplog.records)

    def test_start_and_stop_methods(self):
        consumer = MqttConsumer()
        consumer.client = MagicMock()
        consumer.start()
        consumer.client.connect.assert_called_once_with(consumer.host, consumer.port, 60)
        consumer.client.loop_start.assert_called_once()

        consumer.stop()
        consumer.client.loop_stop.assert_called_once()
        consumer.client.disconnect.assert_called_once()
