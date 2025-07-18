from abc import ABC, abstractmethod
from weather.dtos.weather_request_dto import WeatherRequestDTO

class WeatherClientInterface(ABC):
    @abstractmethod
    def get_weather(self, request_dto: WeatherRequestDTO ):
        pass
