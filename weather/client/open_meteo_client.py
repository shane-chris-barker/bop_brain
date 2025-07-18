import logging
from weather.resolvers.open_meteo_response_resolver import OpenMeteoResponseResolver
from weather.resolvers.weather_response_resolver_interface import WeatherResponseResolverInterface
logger = logging.getLogger(__name__)
import requests
from weather.client.weather_client_interface import WeatherClientInterface
from weather.dtos.weather_request_dto import WeatherRequestDTO

class OpenMeteoClient(WeatherClientInterface):
    def __init__(self, resolver: WeatherResponseResolverInterface = OpenMeteoResponseResolver()):
        self.base_url = "https://api.open-meteo.com/v1/forecast?"
        self.log_prefix = "[🌡️ OPEN METEO CLIENT]"
        self.resolver = resolver

    def get_weather(self, request_dto: WeatherRequestDTO):
        try:
            response = requests.get(self._build_url(request_dto.latitude, request_dto.longitude))
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logger.error(f"{self.log_prefix} Error requesting from Weather API: {err}")
            return None
        weather_forecast_dto = self.resolver.resolve(
            raw=response.json(),
            location=request_dto.location_name
        )

        return weather_forecast_dto

    def _build_url(self, latitude: float, longitude: float) -> str:
        return f"{self.base_url}latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min"
