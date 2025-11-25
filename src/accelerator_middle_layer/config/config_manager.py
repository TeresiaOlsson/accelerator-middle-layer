""" Module for config manager. """

from ..config import AcceleratorConfig
from ..registry.registry_dict import RegistryDict

class ConfigManager:
    def __init__(self, config: AcceleratorConfig):
        self._config = config

        self.backend_registry = RegistryDict({
            backend.name: backend
            for backend in config.backends
        })

    def get_attr(self, attr_name: str):
        return getattr(self._config, attr_name)        
