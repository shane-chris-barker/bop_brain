import pytest
from unittest.mock import MagicMock
from bop_common.enums.hardware_type import HardwareType
from bop_common.dtos.communication_dto import CommunicationDTO
from communication.handlers.incoming_communication_message_handler_interface import IncomingCommunicationMessageHandlerInterface
from communication.handlers.handler_registry import HandlerRegistry

class DummyHandlerA(IncomingCommunicationMessageHandlerInterface):
    def __init__(self):
        self.name = "DummyHandlerA"
class DummyHandlerB(IncomingCommunicationMessageHandlerInterface):
    def __init__(self):
        self.name = "DummyHandlerB"

def make_message_with_input(hardware_type):
    msg = MagicMock(spec=CommunicationDTO)
    msg.input = hardware_type
    return msg

@pytest.fixture(autouse=True)
def clear_registry_before_tests():
    HandlerRegistry.reset_handlers()
    yield
    HandlerRegistry.reset_handlers()

def test_registry_adds_handler():
    HandlerRegistry.register(HardwareType.MIC, DummyHandlerA)
    assert HandlerRegistry._handlers[HardwareType.MIC] is DummyHandlerA

def test_get_handler_returns_instance_of_registered_handler():
    HandlerRegistry.register(HardwareType.MIC, DummyHandlerA)
    msg = make_message_with_input(HardwareType.MIC)
    handler_instance = HandlerRegistry.get_handler_for_message(msg)
    assert isinstance(handler_instance, DummyHandlerA)
    assert handler_instance.name == "DummyHandlerA"

def test_get_handler_raises_if_no_handler_registered():
    msg = make_message_with_input(HardwareType.MIC)
    with pytest.raises(ValueError) as exception:
        HandlerRegistry.get_handler_for_message(msg)
    assert "No handler registered" in str(exception.value)

def test_register_multiple_handlers_and_resolve():
    HandlerRegistry.register(HardwareType.MIC, DummyHandlerA)
    HandlerRegistry.register(HardwareType.TEST_HARDWARE, DummyHandlerB)

    msg_a = make_message_with_input(HardwareType.MIC)
    handler_a = HandlerRegistry.get_handler_for_message(msg_a)
    assert isinstance(handler_a, DummyHandlerA)

    msg_b = make_message_with_input(HardwareType.TEST_HARDWARE)
    handler_b = HandlerRegistry.get_handler_for_message(msg_b)
    assert isinstance(handler_b, DummyHandlerB)