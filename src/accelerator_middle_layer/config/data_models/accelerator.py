"""Configuration model for accelerator."""

from pydantic import BaseModel
from typing import List, Optional
from .backends import Backends


class AcceleratorConfig(BaseModel):

    facility: Optional[str]
    machine: str
    # TODO: data_storage
    backends: Optional[List[Backends]] = None
    #devices: Optional[List[str]] = None
    #families: Optional[List[str]] = None
    # TODO: operational_modes





