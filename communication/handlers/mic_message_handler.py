import logging
logger = logging.getLogger(__name__)
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.incoming_communication_message_handler_interface import \
    IncomingCommunicationMessageHandlerInterface


class MicMessageHandler(IncomingCommunicationMessageHandlerInterface):
    def handle(self, dto: CommunicationDTO):
        logger.info('Mic handler just got the message')