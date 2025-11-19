from typing import TypeVar, Callable, Dict, Type
from pydantic import BaseModel

# Base type variables
DeviceConfigT = TypeVar("DeviceConfigT", bound=BaseModel)
DeviceT = TypeVar("DeviceT")


class DeviceFactory:
    """
    Factory for creating devices using a device config and a backend config.
    """
    # Registry maps: DeviceConfig type -> creator function (takes device + backend)
    _registry: Dict[Type[BaseModel], Callable[[BaseModel, BaseModel], object]] = {}

    def __init__(self, backend_config: BaseModel):
        self.backend = backend_config

    @classmethod
    def register(cls, device_type: Type[DeviceConfigT]):
        """Register a creator function for a device type (shared globally)."""
        def decorator(func: Callable[[DeviceConfigT, BaseModel], DeviceT]):
            cls._registry[device_type] = func
            return func
        return decorator

    def create(self, device_config: BaseModel) -> DeviceT:
        device_type = type(device_config)
        if device_type not in self._registry:
            raise ValueError(f"No creator registered for device type {device_type}")
        creator = self._registry[device_type]
        # Use the backend tied to this factory instance
        return creator(device_config, self.backend)
