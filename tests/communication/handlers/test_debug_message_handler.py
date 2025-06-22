from unittest.mock import patch
from bop_common.enums.hardware_type import HardwareType
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.debug_message_handler import DebugMessageHandler

class TestDebugMessageHandler:

    def test_handle_logs_and_publishes(self):
        handler = DebugMessageHandler()
        dummy_msg = CommunicationDTO(input=HardwareType.TEST_HARDWARE.value, content={'content':'test'})

        with patch("communication.handlers.debug_message_handler.logger") as logger, \
            patch("communication.handlers.debug_message_handler.get_publisher") as mock_get_publisher:

            mock_publisher = mock_get_publisher.return_value
            handler.handle(dummy_msg)

        logger.info.assert_any_call("[🪳 DEBUG HANDLER] just got the message")
        logger.info.assert_any_call("[🪳 DEBUG HANDLER] just got the {} from the factory".format(mock_publisher))
        logger.info.assert_any_call("[🪳 DEBUG HANDLER] just published the message")
        mock_publisher.publish.assert_called_once()
