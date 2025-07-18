from abc import ABC, abstractmethod
from typing import Optional

class IPClientInterface(ABC):
    @abstractmethod
    def get_public_ip(self) -> Optional[str]:
        pass
