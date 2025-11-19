""" Module for config manager. """

from ..config import AcceleratorConfig

class ConfigManager:
    def __init__(self, config: AcceleratorConfig):
        self._config = config

        self.backends_by_name = {
            backend.name: backend
            for backend in getattr(config, "backends", [])
        }

    def get_attr(self, attr_name: str):
        return getattr(self._config, attr_name) 
      

    #def to_dict(self):
    #    return self.config.model_dump(by_alias=True)

    # # update a nested key: "ui.theme" = "light"
    # def update(self, dotted_key: str, value):
    #     section, field = dotted_key.split(".")
    #     obj = getattr(self.config, section)
    #     setattr(obj, field, value)  # Pydantic will validate

    # # save/load
    # def save(self, path="config.json"):
    #     with open(path, "w") as f:
    #         f.write(self.config.model_dump_json(indent=2))

    # def load(self, path="config.json"):
    #     with open(path) as f:
    #         self.config = AppConfig.model_validate_json(f.read())