import unittest
from requests.exceptions import RequestException
from unittest.mock import Mock, patch
from weather.client.open_meteo_client import OpenMeteoClient
from weather.dtos.weather_request_dto import WeatherRequestDTO
from weather.resolvers.weather_response_resolver_interface import WeatherResponseResolverInterface

class OpenMeteoClientTest(unittest.TestCase):
    def setUp(self):
        self.mock_resolver = Mock(spec=WeatherResponseResolverInterface)
        self.client = OpenMeteoClient(self.mock_resolver)
        self.weather_request_dto = WeatherRequestDTO(
            latitude=52.52,
            longitude=13.37,
            location_name='Test'
        )

    @patch("weather.client.open_meteo_client.requests.get")
    def test_get_weather_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'dummy':'data'}
        mock_get.return_value = mock_response
        expected_weather_dto = Mock()
        self.mock_resolver.resolve.return_value = expected_weather_dto

        result = self.client.get_weather(self.weather_request_dto)

        mock_get.assert_called_once_with(
            "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.37&daily=weather_code,temperature_2m_max,temperature_2m_min"
        )
        self.mock_resolver.resolve.assert_called_once_with(
            raw={"dummy": "data"},
            location="Test"
        )
        self.assertEqual(result, expected_weather_dto)

    @patch("weather.client.open_meteo_client.requests.get")
    def test_get_weather_failure_returns_none(self, mock_get):
        mock_get.side_effect = RequestException("Connection error")
        result = self.client.get_weather(self.weather_request_dto)
        self.assertIsNone(result)