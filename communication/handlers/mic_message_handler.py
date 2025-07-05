import logging
from intent.factories.intent_resolver_factory import get_intent_resolver
logger = logging.getLogger(__name__)
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.incoming_communication_message_handler_interface import \
    IncomingCommunicationMessageHandlerInterface

class MicMessageHandler(IncomingCommunicationMessageHandlerInterface):
    def __init__(self) -> None:
        self.intent_resolver = get_intent_resolver()
        self.log_prefix = "[🎤 MIC HANDLER]"

    def handle(self, dto: CommunicationDTO):
        logger.info(f"{self.log_prefix} just picked up a message!")
        self.intent_resolver.resolve(dto)