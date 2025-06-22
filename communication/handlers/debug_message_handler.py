import logging
logger = logging.getLogger(__name__)
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.event_type import EventType
from bop_common.dtos.event_dto import EventDTO
from communication.handlers.incoming_communication_message_handler_interface import \
    IncomingCommunicationMessageHandlerInterface
from events.factories.publisher_factory import get_publisher

class DebugMessageHandler(IncomingCommunicationMessageHandlerInterface):
    def __init__(self) -> None:
        self.log_prefix = "[🪳 DEBUG HANDLER]"
    def handle(self, message: CommunicationDTO):
        logger.info(f'{self.log_prefix} just got the message')
        publisher = get_publisher()
        event_dto = EventDTO(event_type=EventType.BOP_DANCE)
        logger.info(f'{self.log_prefix} just got the {publisher} from the factory')
        publisher.publish(event_dto)
        logger.info(f'{self.log_prefix} just published the message')
