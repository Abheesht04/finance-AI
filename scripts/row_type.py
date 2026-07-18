from enum import Enum, auto


class RowType(Enum):

    UNKNOWN = auto()

    HEADER = auto()

    KEY_VALUE = auto()

    SECTION_HEADER = auto()

    TABLE_HEADER = auto()

    TABLE_ROW = auto()

    TEXT = auto()
