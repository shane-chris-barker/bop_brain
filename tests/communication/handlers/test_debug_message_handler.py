from unittest.mock import patch
from bop_common.enums.hardware_type import HardwareType
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.debug_message_handler import DebugMessageHandler

class TestDebugMessageHandler:

    def test_handle_logs_message(self):
        handler = DebugMessageHandler()
        dummy_msg = CommunicationDTO(input=HardwareType.TEST_HARDWARE.value, content={'content':'test'})

        with patch("communication.handlers.debug_message_handler.logger") as logger:
            handler.handle(dummy_msg)
        logger.info.assert_called_once_with('debug handler just got the message')

