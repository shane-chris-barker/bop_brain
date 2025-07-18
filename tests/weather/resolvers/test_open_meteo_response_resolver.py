import unittest
from weather.resolvers.open_meteo_response_resolver import OpenMeteoResponseResolver
from bop_common.dtos.weather.daily_forecast_dto import DailyForecastDTO
from bop_common.dtos.weather.weather_data_dto import WeatherDataDTO

class TestOpenMeteoResponseResolver(unittest.TestCase):
    def setUp(self):
        self.resolver = OpenMeteoResponseResolver()

    def test_resolve_with_known_weather_code(self):
        raw_response = {
            "daily": {
                "time": ["2025-07-17", "2025-07-18"],
                "temperature_2m_max": [25, 23],
                "weather_code": [0, 3]  # Clear sky and Overcast
            }
        }

        location = "Test City"
        result = self.resolver.resolve(raw=raw_response, location=location)

        expected_forecast = WeatherDataDTO(
            city=location,
            forecast=[
                DailyForecastDTO(date="2025-07-17", temperature=25, description="Clear sky"),
                DailyForecastDTO(date="2025-07-18", temperature=23, description="Overcast")
            ]
        )

        self.assertEqual(result, expected_forecast)
        self.assertEqual(result.city, location)
        self.assertEqual(result.forecast, expected_forecast.forecast)
