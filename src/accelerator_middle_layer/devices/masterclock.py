""" Module for masterclock. """

from pydantic import BaseModel
from typing import Optional

class SignalModel(BaseModel)
    readback: str
    setpoint: Optional[str] = None


class MasterclockModel(BaseModel)
    frequency: SignalModel

class MasterClock(StandardReadable):

    def __init__(self, readback: str, setpoint: Optional[str] = None, backend: str):

        frequency = Signal(backend)

        self._readback = readback
        if setpoint:
            self._setpoint = setpoint

@DeviceFactory.register(MasterclockModel)
def create_masterclock(schema: MasterclockModel) -> MasterClock:
    return MasterClock(readback=schema.readback, setpoint=schema.setpoint)


from typing import TypeVar, Callable, Dict, Type, Generic

SchemaT = TypeVar("SchemaT", bound=BaseModel)
DomainT = TypeVar("DomainT")

class DeviceFactory:
    _registry: Dict[Type[BaseModel], Callable[[BaseModel]], object] = {}

    @classmethod
    def register(cls, schema_type: Type[SchemaT]):
        """Decorator to register a creation function for a schema."""
        def decorator(func: Callable[[SchemaT], DomainT]) -> Callable[[SchemaT], DomainT]:
            cls._registry[schema_type] = func
            return func
        return decorator
    
    @classmethod
    def create(cls, schemaT) -> DomainT:
        schema_type: Type[BaseModel] = type(schema)
        if schema_type not in cls._registry:
            raise ValueError("No creator registered for {schema_type}")
        creator = cls._registry[schema_type]
        return creator(schema)
    


