from bop_common.dtos.communication_dto import CommunicationDTO

class IntentStrategyInterface:
    def matches(self, text: str) -> bool:
        raise NotImplementedError()

    def execute(self, dto: CommunicationDTO):
        raise NotImplementedError()
