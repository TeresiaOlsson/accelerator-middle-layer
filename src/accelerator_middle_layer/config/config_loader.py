""" Loaders to read in configuration."""

from abc import ABC, abstractmethod
from typing import Type, TypeVar, Dict, List
from yaml import safe_load
import json
from pydantic import BaseModel
from pathlib import Path

# Define a required type for the config
ConfigT = TypeVar("ConfigT", bound=BaseModel)


class ConfigLoader(ABC):
    """Abstract base class for config loaders."""

    source_types: List[str] = [] # File extension, database, etc.

    # Pass the model to the loader allows to load into any model.
    # This could be used to load parts of a nested model.
    @classmethod
    @abstractmethod
    def load(cls, source: str, model: Type[ConfigT]) -> ConfigT:
        """Load config into given pydantic model."""
        raise NotImplementedError


class YamlLoader(ConfigLoader):
    """Load from a yaml file."""

    source_types = ["yaml","yml"]

    @classmethod
    def load(cls, source: str, model: Type[ConfigT]) -> ConfigT:
        with open(source, "r") as f:
            data = safe_load(f)
        return model(**data)


class JsonLoader(ConfigLoader):
    """Load from a json file."""

    source_types = ["json"]

    @classmethod
    def load(cls, source: str, model: Type[ConfigT]) -> ConfigT:
        with open(source, "r") as f:
            data = json.load(f)
        return model(**data)

# Loader registry
_loader_registry: Dict[str, Type[ConfigLoader]] = {}

def register_loader(loader_cls: Type[ConfigLoader]):
    """Register a loader class and it source types."""

    for source in getattr(loader_cls, "source_types", []):
        if source:
            _loader_registry[source.lower()] = loader_cls

# Register default loader
for loader in [YamlLoader, JsonLoader]:
    register_loader(loader)

def load_config(source: str, model: Type[ConfigT]) -> ConfigT:
    """ Load the config from a registered source. """

    loader_cls = None
    path = Path(source)

    if path.exists():
        # Use file extension
        extension = path.suffix.lower().lstrip(".")
        loader_cls = _loader_registry.get(extension)

    if not loader_cls:
        raise ValueError(f"No loader registered for source '{source}'")

    return loader_cls.load(source, model)