from dataclasses import dataclass

@dataclass
class WeatherRequestDTO:
    location_name: str
    latitude: float
    longitude: float
