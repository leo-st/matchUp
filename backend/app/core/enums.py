from enum import Enum

class ExtendedEnum(Enum):

    @classmethod
    def value_list(cls):
        return list(map(lambda c: c.value, cls))
    