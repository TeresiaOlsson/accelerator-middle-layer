""" Configuration class for accelerator and families."""

from pydantic import BaseModel
from typing import List, Optional
from .backends import BackendUnion
#from .device import DeviceConfig


class AcceleratorConfig(BaseModel):

    facility: Optional[str]
    machine: str
    # TODO: data_storage
    backends: Optional[List[BackendUnion]] = None
    devices: Optional[List[str]] = None
    families: Optional[List[str]] = None
    # TODO: operational_modes


class FamilyConfig(BaseModel):
    name: str
    devices: list[str]


