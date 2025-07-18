from weather.resolvers.weather_response_resolver_interface import WeatherResponseResolverInterface
from bop_common.dtos.weather.daily_forecast_dto import DailyForecastDTO
from bop_common.dtos.weather.weather_data_dto import WeatherDataDTO

WEATHER_CODE_MAP = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

class OpenMeteoResponseResolver(WeatherResponseResolverInterface):
    def __init__(self):
        self.weather_code_map = WEATHER_CODE_MAP

    def resolve(self, raw: dict, location: str) -> WeatherDataDTO:
        forecast = []
        daily = raw["daily"]

        for i in range(len(daily['time'])):
            forecast.append(DailyForecastDTO(
                date=daily['time'][i],
                temperature=daily['temperature_2m_max'][i],
                description=self._resolve_weather_code(daily['weather_code'][i])
            ))
        return WeatherDataDTO(city=location, forecast=forecast)

    def _resolve_weather_code(self, code: str) -> str:
        return self.weather_code_map.get(code, "Unknown")
