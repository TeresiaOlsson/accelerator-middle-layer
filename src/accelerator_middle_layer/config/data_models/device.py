""" Configuration classes for devices."""

from pydantic import BaseModel, Field
from abc import ABC
from typing import Optional

# TODO: figure out what is required for a device and what is same/different
# depdening on the control system
# It needs to also be possible to configure devices from external modules
# in the same way.

class DeviceConfig(BaseModel, ABC):
    name: str
    # What is required here?


class MagnetConfig(DeviceConfig):
    magnet_type: str = Field(alias="type")
    power_supply: Optional[str] = None
