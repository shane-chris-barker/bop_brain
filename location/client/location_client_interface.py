from abc import ABC, abstractmethod
from location.dtos.location_dto import LocationDTO

class LocationClientInterface(ABC):
    @abstractmethod
    def get_location(self) -> LocationDTO:
        raise NotImplementedError()

    def ready(self) -> bool:
        raise NotImplementedError()
