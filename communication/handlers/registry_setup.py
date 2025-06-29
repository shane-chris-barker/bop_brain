from bop_common.enums.hardware_type import HardwareType
from communication.handlers.mic_message_handler import MicMessageHandler
from communication.handlers.debug_message_handler import DebugMessageHandler
from communication.handlers.camera_message_handler import CameraMessageHandler
from communication.handlers.handler_registry import HandlerRegistry

def register_handlers():
    HandlerRegistry.register(HardwareType.MIC, MicMessageHandler)
    HandlerRegistry.register(HardwareType.TEST_HARDWARE, DebugMessageHandler)
    HandlerRegistry.register(HardwareType.CAMERA, CameraMessageHandler)
