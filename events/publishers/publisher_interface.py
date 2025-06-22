from abc import ABC, abstractmethod
from bop_common.dtos.event_dto import EventDTO

class PublisherInterface(ABC):
    @abstractmethod
    def publish(self, message: EventDTO) -> None:
        pass