import unittest
from unittest.mock import MagicMock, patch
from bop_common.dtos.event_dto import EventDTO
from intent.strategies.weather_report_strategy import WeatherReportStrategy
from bop_common.enums.event_type import EventType
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.hardware_type import HardwareType

class TestWeatherReportStrategy(unittest.TestCase):
    def setUp(self):
        self.mock_weather_client = MagicMock()
        self.strategy = WeatherReportStrategy(client=self.mock_weather_client)

    def test_matches_returns_true_when_keywords_in_text(self):
        self.assertTrue(self.strategy.matches("What is the weather today?"))
        self.assertTrue(self.strategy.matches("What is the forecast today?"))

    def test_matches_returns_false_when_keywords_not_in_text(self):
        self.assertFalse(self.strategy.matches("Bop is happy!"))

    @patch("intent.strategies.weather_report_strategy.get_publisher")
    @patch("intent.strategies.weather_report_strategy.IPGeoLocationClient")
    def test_execute_publishes_weather_event(self, mock_location_client_cls, mock_get_publisher):
        mock_publisher = MagicMock()
        mock_get_publisher.return_value = mock_publisher

        mock_location_client = MagicMock()
        mock_location_client.ready.return_value = True
        mock_location = MagicMock()
        mock_location.latitude = 52.95
        mock_location.longitude = -52.95
        mock_location.city = "Test City"
        mock_location_client.get_location.return_value = mock_location
        mock_location_client_cls.return_value = mock_location_client

        mock_weather = MagicMock()
        mock_weather.to_dict.return_value = {"temperature":22, "description":"Sunny"}
        self.mock_weather_client.get_weather.return_value = mock_weather

        strategy = WeatherReportStrategy(client=self.mock_weather_client, location_client=mock_location_client)
        dto = CommunicationDTO(input=HardwareType.MIC, content={"text":"Can I have the weather please?"})
        strategy.execute(dto)

        self.mock_weather_client.get_weather.assert_called_once()
        mock_publisher.publish.assert_called_once()

        published_event: EventDTO = mock_publisher.publish.call_args[0][0]
        self.assertEqual(published_event.event_type, EventType.BOP_WEATHER_REPORT)
        self.assertEqual(published_event.payload, {"temperature":22, "description":"Sunny"})
