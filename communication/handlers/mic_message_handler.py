import logging
logger = logging.getLogger(__name__)
from bop_common.dtos.event_dto import EventDTO
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.event_type import EventType
from communication.handlers.incoming_communication_message_handler_interface import \
    IncomingCommunicationMessageHandlerInterface
from events.factories.publisher_factory import get_publisher

class MicMessageHandler(IncomingCommunicationMessageHandlerInterface):
    def __init__(self) -> None:
        self.keyword_event_map = {
            "dance": EventType.BOP_DANCE,
            "happy": EventType.BOP_HAPPY,
            "sad": EventType.BOP_SAD,
            "angry": EventType.BOP_ANGRY,
            "test": EventType.BOP_HAPPY,
        }
        self.log_prefix = "[🎤 MIC HANDLER]"

    def handle(self, dto: CommunicationDTO):
        text = dto.content.get("text", "").lower()
        logger.info(f"{self.log_prefix} is checking for the word(s): {text}")

        for keyword, event_type in self.keyword_event_map.items():
            if keyword in text:
                event_dto = EventDTO(event_type=event_type)
                publisher = get_publisher()
                publisher.publish(event_dto)
                logger.info(f"{self.log_prefix} Dispatched event:{event_type} for keyword:{keyword}")
                break