""" Configuration class for accelerator and families."""

from pydantic import BaseModel
from typing import Dict, List, Optional
from .backends import BackendConfig
from .device import DeviceConfig


class AcceleratorConfig(BaseModel):

    facility: Optional[str]
    machine: str
    # TODO: data_storage
    backends: Optional[Dict[str, BackendConfig]] = None
    devices: Optional[Dict[str, DeviceConfig]] = None # Should this be a list or a dict?
    families: Optional[Dict[str, List[str]]] = None
    # TODO: operational_modes


class FamilyConfig(BaseModel):
    name: str
    devices: list[str]
    