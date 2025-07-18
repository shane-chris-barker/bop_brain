from bop_common.enums.event_type import EventType
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.dtos.event_dto import EventDTO
from intent.strategies.Intent_strategy_interface import IntentStrategyInterface
from events.factories.publisher_factory import get_publisher

class SadIntentStrategy(IntentStrategyInterface):
    def matches(self, text: str) -> bool:
        return "sad" in text
    def execute(self, dto: CommunicationDTO):
        event = EventDTO(event_type=EventType.BOP_SAD)
        get_publisher().publish(event)
