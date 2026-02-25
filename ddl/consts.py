from enum import Enum, auto


class DDLTokenType(Enum):
    INIT = auto()
    SQL = auto()
    CRATE = auto()
    FIELD = auto()
    CREATE_TABLE = auto()
    COMMENT = auto()
    OPTION = auto()

    TABLE_NAME = auto()
    FIELD_NAME = auto()
    FIELD_TYPE = auto()
    FIELD_LENGTH = auto()
    PRIMARY_KEY = auto()
    PRIMARY_KEY_VALUE = auto()
    COMMAND = auto()


class Status(Enum):
    BASE_INIT = auto()
    BASE_SQL = auto()
    BASE_CREATE = auto()
    BASE_FIELD = auto()
    BASE_FIELD_OPTION = auto()
    BASE_OPTION = auto()
    BASE_PRIMARY_KEY = auto()


class TableConstants:
    CLASS_NAME = "{class_name}"
    TABLE_NAME = "{table_name}"
    FIELD_NAME = "{field_name}"
    FIELD_TYPE = "{field_type}"

    DB_TYPE_2_PY = {
        "varchar": "String",
        "int": "Integer",
        "datetime": "DateTime",
        "decimal": "Float",
    }
