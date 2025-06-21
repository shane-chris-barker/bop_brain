from abc import ABC, abstractmethod
from bop_common.dtos.communication_dto import CommunicationDTO

class ConsumerInterface(ABC):
    @abstractmethod
    def consume(self, message: CommunicationDTO) -> None:
        pass