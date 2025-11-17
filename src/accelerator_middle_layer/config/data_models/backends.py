""" Configuration models for backends."""

from pydantic import BaseModel
from abc import ABC
from typing import Hashable, Optional, Union
from enum import Enum


class BackendConfig(BaseModel, ABC):
    name: Hashable


class TANGOConfig(BackendConfig):
    host: Hashable


class EPICSType(Enum):

    CA = 'CA' # Channel Access
    PV = 'PV' # PV Access


class EPICSConfig(BackendConfig):
    access_type: EPICSType
    pv_prefix: Optional[Hashable] = ""


class DOOCSConfig(BackendConfig):
    pass


class SimulationEngine(Enum):
    PYAT = 'pyat'


class SimulatorConfig(BackendConfig):
    type: SimulationEngine
    model: str  # Path to the lattice model.
