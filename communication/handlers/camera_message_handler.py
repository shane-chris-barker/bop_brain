import logging
logger = logging.getLogger(__name__)
from bop_common.dtos.event_dto import EventDTO
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.event_type import EventType
from communication.handlers.incoming_communication_message_handler_interface import \
    IncomingCommunicationMessageHandlerInterface
from events.factories.publisher_factory import get_publisher

class CameraMessageHandler(IncomingCommunicationMessageHandlerInterface):
    def __init__(self):
        self.log_prefix = '[📷 CAMERA HANDLER]'

    def handle(self, dto: CommunicationDTO):
        logger.info(f"{self.log_prefix} Received message.")
        # TODO - Image processing here - Maybe check if we have video or image etc
        # for now, just emit a bop_dance or something so we know it's working
        event_dto = EventDTO(event_type=EventType.BOP_HAPPY)
        publisher = get_publisher()
        publisher.publish(event_dto)
        logger.info(f"{self.log_prefix} Published message.")

