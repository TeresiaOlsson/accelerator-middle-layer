""" Configuration models for backends."""

from pydantic import BaseModel, Field
from abc import ABC
from typing import Hashable, Optional, Union, Literal, Annotated
from enum import Enum


class BackendConfig(BaseModel, ABC):
    name: str
    type: str


class TangoConfig(BackendConfig):
    type: Literal["tango"]
    host: Hashable


class EpicsProtocol(Enum):
    CA = "ca"
    PVA = "pva"

    def __repr__(self):
        return self.value 

class EpicsConfig(BackendConfig):
    type: Literal["epics"]
    protocol: Optional[EpicsProtocol] = EpicsProtocol.CA
    prefix: Optional[Hashable] = ""

    class Config:
        use_enum_values = True

Backends = Annotated[
    Union[TangoConfig, EpicsConfig],
    Field(discriminator='type')
]

# class SimulationEngine(Enum):
#     PYAT = 'pyat'


# class SimulatorConfig(BackendConfig):
#     type: SimulationEngine
#     model: str  # Path to the lattice model.

