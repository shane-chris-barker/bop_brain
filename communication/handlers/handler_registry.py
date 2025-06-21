from typing import Dict, Type
from bop_common.dtos.communication_dto import CommunicationDTO
from bop_common.enums.hardware_type import HardwareType
from communication.handlers.incoming_communication_message_handler_interface import IncomingCommunicationMessageHandlerInterface

class HandlerRegistry:
    _handlers: Dict[HardwareType, Type[IncomingCommunicationMessageHandlerInterface]] = {}

    @classmethod
    def register(cls, hardware_type: HardwareType, handler_cls: Type[IncomingCommunicationMessageHandlerInterface]) -> None:
        cls._handlers[hardware_type] = handler_cls

    @classmethod
    def get_handler_for_message(cls, message: CommunicationDTO) -> IncomingCommunicationMessageHandlerInterface:
        handler_cls = cls._handlers.get(message.input)
        if handler_cls:
            return handler_cls()
        else:
            raise ValueError(f"No handler registered for input {message.input}")

    @classmethod
    def reset_handlers(cls) -> None:
        cls._handlers.clear()