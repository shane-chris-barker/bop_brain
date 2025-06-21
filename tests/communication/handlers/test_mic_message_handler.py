from unittest.mock import patch
from bop_common.enums.hardware_type import HardwareType
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.mic_message_handler import MicMessageHandler

class TestMicMessageHandler:

    def test_handle_detects_keywords_and_logs_dispatch(self):
        handler = MicMessageHandler()
        dummy_message = CommunicationDTO(
            input=HardwareType.TEST_HARDWARE,
            content={'text':'shut up and dance'}
        )

        with patch("communication.handlers.mic_message_handler.logger") as mock_logger:
            handler.handle(dummy_message)
            mock_logger.info.assert_any_call("[🎤 MIC HANDLER] is checking for the word(s): shut up and dance")
            mock_logger.info.assert_any_call("[🎤 MIC HANDLER] Dispatched event:EventType.BOP_DANCE for keyword:dance")

    def test_handle_no_match_logs_no_match(self):
        handler = MicMessageHandler()
        dummy_message = CommunicationDTO(
            input=HardwareType.TEST_HARDWARE,
            content={'text':'oogie boogie'}
        )
        with patch("communication.handlers.mic_message_handler.logger") as mock_logger:
            handler.handle(dummy_message)
            mock_logger.info.assert_any_call("[🎤 MIC HANDLER] is checking for the word(s): oogie boogie")




