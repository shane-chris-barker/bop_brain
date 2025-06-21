from bop_common.dtos.communication_dto import CommunicationDTO

class IncomingCommunicationMessageHandlerInterface:
    def handle(self, dto: CommunicationDTO):
        pass