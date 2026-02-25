from ddl.consts import Status, DDLTokenType


class DDLLexer:
    def __init__(self):
        self.results = []
        self.filed_prefix = "vid"

    def tokenize(self, script: str, sts: Status):
        status = DDLTokenType.INIT
        result = DDLTokenResult()

        

class DDLTokenResult:
    def __init__(self):
        self.status = Status.BASE_INIT
        self.text = []
        self.token_type: DDLTokenType = DDLTokenType.INIT

    def append(self, value: str):
        self.text.append(value)

    def is_varchar(self) -> bool:
        return "".join(self.text) == "va"

    def length(self) -> int:
        return len(self.text)

    def __str__(self):
        return "".join(self.text)


class DDLInfo:
    def __init__(self):
        self.table_name = None
        self.primary_key = None
        self.comment = None


class DDLFieldInfo:
    def __init__(self):
        self.field_name = None
        self.field_type = None
        self.field_length = None
        self.comment = None
