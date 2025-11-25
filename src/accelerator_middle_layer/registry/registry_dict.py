""" Module for registry dictionary. """

# Attributes that are reserved for dicts, e.g keys, items etc.
#DICT_RESERVED_KEYS = vars(dict).keys()

#TODO: functionality needs to be added for autocompletion. See prodict.

class RegistryDict(dict):

    def __init__(self, *args, **kwargs):

        # Initialise the dict
        super().__init__(*args, **kwargs)

        # Mirror keys that are valid identifiers as attributes
        for k, v in self.items():
            if isinstance(k, str) and k.isidentifier():
                setattr(self, k, v)
