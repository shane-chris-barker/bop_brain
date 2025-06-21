from unittest.mock import patch
from bop_common.enums.hardware_type import HardwareType
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.mic_message_handler import MicMessageHandler

class TestMicMessageHandler:

    def test_handle_logs_message(self):
        handler = MicMessageHandler()
        dummy_msg = CommunicationDTO(input=HardwareType.TEST_HARDWARE.value, content={'text':'hello'})

        with patch("communication.handlers.mic_message_handler.logger") as logger:
            handler.handle(dummy_msg)
        logger.info.assert_called_once_with('Mic handler just got the message')
