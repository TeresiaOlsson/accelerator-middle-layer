""" Module for the accelerator object."""

from .config import AcceleratorConfig, ConfigManager
from .config.config_loader import load_config
import yaml
#from typing import Hashable

#from .utils import WildcardDict


class Accelerator():

    def __init__(self, config: AcceleratorConfig):

        # Create the config manager
        self._config_manager = ConfigManager(config)

        # TODO: create device/family factory

        #self._facility = config.facility
        #self._machine = config.machine
        #self._backends = {item.name: item for item in config.backends} 
        # self._devices = WildcardDict(config.devices) # Dict which can use wildcards
        # self._families = config.families

    @property
    def facility(self):
        return self._config_manager.get_attr("facility")

    @property
    def machine(self):
        return self._config_manager.get_attr("machine")

    @property
    def backends(self):
        backends = self._config_manager.backend_registry
        if backends:
            return backends
        else:
            print('No backends have been configured.')

    # @property
    # def devices(self):
    #     if self._devices:
    #         return self._devices
    #     else:
    #         print('No devices have been configured.')

    # @property
    # def families(self):
    #     if self._families:
    #         return self._families
    #     else:
    #         print('No families have been configured.')


    def __repr__(self):
        """Pretty printing of the accelerator configuration."""

        #TODO: make this nicer.

        backend_details = "\n".join(
            f"  - {name}: \n{yaml.dump(backend.model_dump(mode='json'), sort_keys=False, indent=4)}"
            for name, backend in self.backends.items()
        )

        return (
            f"Facility: {self.facility}\n"
            f"Machine: {self.machine}\n"
            f"Backends:\n{backend_details}"
        )
    

    def load(source: str) -> "Accelerator":
        """Create accelerator by loading the config."""

        return Accelerator(load_config(source, AcceleratorConfig))

