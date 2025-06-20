from abc import ABC, abstractmethod

class ConsumerInterface(ABC):
    @abstractmethod
    def consume(self) -> None:
        pass