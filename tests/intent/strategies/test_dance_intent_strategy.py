import unittest
from unittest.mock import MagicMock, patch
from intent.strategies.dance_intent_strategy import DanceIntentStrategy
from bop_common.enums.event_type import EventType
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.hardware_type import HardwareType

class TestDanceIntentStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = DanceIntentStrategy()

    def test_matches_returns_true_when_dance_string_in_text(self):
        self.assertTrue(self.strategy.matches("Bop, dance"))

    def test_matches_returns_false_when_dance_string_not_in_text(self):
        self.assertFalse(self.strategy.matches("Bop is still!"))

    @patch("intent.strategies.dance_intent_strategy.get_publisher")
    def test_execute_publishes_dance_event(self, mock_get_publisher):
        mock_publisher = MagicMock()
        mock_get_publisher.return_value = mock_publisher
        dto = CommunicationDTO(
            input=HardwareType.MIC,
            content={'text': 'Bop, dance!'}
        )
        self.strategy.execute(dto)
        mock_publisher.publish.assert_called_once()
        published_event = mock_publisher.publish.call_args[0][0]
        self.assertEqual(published_event.event_type, EventType.BOP_DANCE)
