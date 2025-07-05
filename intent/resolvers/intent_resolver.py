from typing import List
from intent.strategies.Intent_strategy_interface import IntentStrategyInterface
from bop_common.dtos.communication_dto import CommunicationDTO

class IntentResolver:
    def __init__(self, strategies: List[IntentStrategyInterface]) -> None:
        self.strategies = strategies

    def resolve(self, dto: CommunicationDTO) -> None:
        text = dto.content.get("text", "").lower()
        for strategy in self.strategies:
            if strategy.matches(text):
                strategy.execute(dto)
                return
