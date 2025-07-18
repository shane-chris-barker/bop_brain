from dataclasses import dataclass

@dataclass
class LocationDTO:
    city: str
    district: str
    zipcode: str
    latitude: float
    longitude: float
    country: str
    continent: str
