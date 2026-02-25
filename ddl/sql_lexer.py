from ddl.consts import DDLTokenType, Status


class TokenResult:
    def __init__(self):
        self.status = Status
        self.text = []
        self.token_type = DDLTokenType.INIT
        self._is_varchar = None

    def append(self, ch):
        self.text.append(ch)

    def is_varchar(self):
        return "".join(self.text) == "va"

    def length(self):
        return len(self.text)

    def __str__(self):
        return "".join(self.text)


class SqlLexer:

    def __init__(self):
        self.results: list[TokenResult] = []

    def tokenize(self, script: str, sts: Status = Status.BASE_INIT, add=False):
        status = DDLTokenType.INIT
        result = TokenResult()
        is_comma_in_brace_field = 0

        for value in script:
            if status == DDLTokenType.INIT:
                result = self.init_token(value, result, sts, add)
                status = result.token_type

            elif status == DDLTokenType.CREATE_TABLE:
                if value == '(':
                    status = DDLTokenType.INIT
                    self.tokenize(result.__str__(), Status.BASE_CREATE, True)
                else:
                    result.append(value)

            elif status in (DDLTokenType.TABLE_NAME, DDLTokenType.FIELD_NAME):
                if value == '`':
                    status = DDLTokenType.INIT
                    result.append(value)
                elif self.is_letter(value):
                    result.append(value)

            elif status == DDLTokenType.FIELD:
                if value == '(':
                    is_comma_in_brace_field += 1
                    result.append(value)
                elif value == ')':
                    is_comma_in_brace_field -= 1
                    result.append(value)
                elif value == ',' and is_comma_in_brace_field == 0:
                    status = DDLTokenType.INIT
                    self.tokenize(result.__str__(), Status.BASE_FIELD, True)
                else:
                    result.append(value)

            elif status == DDLTokenType.FIELD_TYPE:
                if (
                        value in ('t', 'l', 'e', 'r')
                        and not result.is_varchar()
                ):
                    status = DDLTokenType.INIT
                    result.append(value)
                else:
                    result.append(value)

            elif status == DDLTokenType.FIELD_LENGTH:
                if value == ')':
                    status = DDLTokenType.INIT
                    result.append(value)
                else:
                    result.append(value)

            elif status == DDLTokenType.COMMENT:
                if value == "'":
                    status = DDLTokenType.INIT
                    result.text.append(value)
                else:
                    result.text.append(value)

            elif status == DDLTokenType.PRIMARY_KEY:
                if value == ')':
                    status = DDLTokenType.INIT
                    result.append(value)

                    if self.is_primary_key(value):
                        result.token_type = DDLTokenType.PRIMARY_KEY_VALUE
                        result.append(value)
                else:
                    result.append(value)

            elif status == DDLTokenType.PRIMARY_KEY_VALUE:
                if value == '`':
                    status = DDLTokenType.INIT
                else:
                    result.append(value)

            elif status == DDLTokenType.COMMAND:
                if self.is_letter(value):
                    result.append(value)
                else:
                    status = DDLTokenType.INIT

        if result.length() > 0:
            self.results.append(result)

        return self.results

    def init_token(self, value: str, result: TokenResult, sts: Status = Status.BASE_INIT, add=False):

        if result.length() > 0:
            if add:
                self.results.append(result)
            result = TokenResult()

        if value == 'P' and sts == Status.BASE_INIT:
            result.token_type = DDLTokenType.PRIMARY_KEY
            result.append(value)

        elif value == 'C' and sts == Status.BASE_INIT:
            result.token_type = DDLTokenType.CREATE_TABLE
            result.append(value)

        elif value == '`' and sts == Status.BASE_CREATE:
            result.token_type = DDLTokenType.TABLE_NAME
            result.append(value)

        elif value == '`' and sts == Status.BASE_INIT:
            result.token_type = DDLTokenType.FIELD
            result.append(value)

        elif value == '`' and sts == Status.BASE_FIELD:
            result.token_type = DDLTokenType.FIELD_NAME
            result.append(value)

        elif value == '`' and sts == Status.BASE_PRIMARY_KEY:
            result.token_type = DDLTokenType.PRIMARY_KEY
            result.append(value)

        elif value in ('i', 'd', 'v') and sts == Status.BASE_FIELD:
            result.token_type = DDLTokenType.FIELD_TYPE
            result.append(value)

        elif value == '(' and sts == Status.BASE_FIELD:
            result.token_type = DDLTokenType.FIELD_LENGTH
            result.append(value)

        elif value == "'" and sts == Status.BASE_FIELD:
            result.token_type = DDLTokenType.COMMENT
            result.append(value)

        elif self.is_letter(value):
            result.token_type = DDLTokenType.COMMAND
            result.append(value)

        else:
            result.token_type = DDLTokenType.INIT

        return result

    def is_primary_key(self, value: str):
        if not self.is_letter(value):
            return False

        primary_key = "`PRIMARY KEY ("
        for c in primary_key:
            if c == value:
                return False

        return True

    def is_letter(self, value: str):
        return value.isalpha() or value == "_"
