""" Module for the AO and registry functionality."""

from ..config import AcceleratorConfig
from .utils import WildcardDict

class Accelerator():

    def __init__(self, config: AcceleratorConfig):

        self._facility = config.facility
        self._machine = config.machine
        self._backends = config.backends
        self._devices = WildcardDict(config.devices) # Dict which can use wildcards
        self._families = config.families


    @property
    def facility(self):
        return self._facility

    @property
    def machine(self):
        return self._machine

    @property
    def backends(self):
        if self._backends:
            return self._backends
        else:
            print('No backends have been configured.')


    @property
    def devices(self):
        if self._devices:
            return self._devices
        else:
            print('No devices have been configured.')

    @property
    def families(self):
        if self._families:
            return self._families
        else:
            print('No families have been configured.')

    def __str__(self):
        """Pretty printing of the accelerator configuration."""
        pass
