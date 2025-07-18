import logging
from typing import Optional
logger = logging.getLogger(__name__)
from location.client.ip_geo_location_client import IPGeoLocationClient
from location.dtos.location_dto import LocationDTO
from weather.client.open_meteo_client import OpenMeteoClient
from bop_common.enums.event_type import EventType
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.dtos.event_dto import EventDTO
from intent.strategies.Intent_strategy_interface import IntentStrategyInterface
from events.factories.publisher_factory import get_publisher
from weather.dtos.weather_request_dto import WeatherRequestDTO

class WeatherReportStrategy(IntentStrategyInterface):
    def __init__(self, client: OpenMeteoClient, location_client: Optional[IPGeoLocationClient] = None):
        self.client = client
        self.location_client = location_client or IPGeoLocationClient()
        self.log_prefix = "[🌡️ WEATHER REPORT STRATEGY]"

    def matches(self, text: str) -> bool:
        return "weather" in text or 'forecast' in text

    def execute(self, dto: CommunicationDTO):
        logger.info(f"{self.log_prefix} executed!")
        if self.location_client.ready():
            location : LocationDTO = self.location_client.get_location()
            weather_request_dto = WeatherRequestDTO(
                latitude=location.latitude,
                longitude=location.longitude,
                location_name=location.city
            )
            weather = self.client.get_weather(weather_request_dto)
            event_dto = EventDTO(event_type=EventType.BOP_WEATHER_REPORT, payload=weather.to_dict())
            get_publisher().publish(event_dto)
