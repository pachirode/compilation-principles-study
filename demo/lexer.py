from dataclasses import dataclass

from .consts import TokenType


class Result:
    def __init__(self) -> None:
        self.token_type: TokenType = TokenType.INIT
        self.text: list[str] = []

    def append(self, ch):
        self.text.append(ch)

    def get_text(self) -> str:
        return ''.join(self.text)


class TestLexer:

    def __init__(self):
        self.results = []

    def tokenize(self, script: str):
        status = TokenType.INIT
        result = Result()

        for value in script:
            if status == TokenType.INIT:
                result = self.init_token(value, result)
                status = result.token_type

            elif status == TokenType.VAR:
                if self._is_letter(value):
                    result.append(value)
                else:
                    result = self.init_token(value, result)
                    status = result.token_type

            elif status == TokenType.GE:
                if value == '=':
                    result.append(value)
                else:
                    result = self.init_token(value, result)
                    status = result.token_type

            elif status == TokenType.VAL:
                if self._is_digit(value):
                    result.append(value)
                else:
                    result = self.init_token(value, result)
                    status = result.token_type

        if result.text:
            self.results.append(result)

        return self.results

    def init_token(self, value, result) -> Result:
        if result.text:
            self.results.append(result)
            result = Result()

        if self._is_letter(value):
            result.token_type = TokenType.VAR
            result.append(value)

        elif self._is_digit(value):
            result.token_type = TokenType.VAL
            result.append(value)

        elif value == "=":
            result.token_type = TokenType.GE
            result.append(value)

        else:
            result.token_type = TokenType.INIT

        return result

    def _is_letter(self, value):
        return 'A' <= value <= 'z'

    def _is_digit(self, value):
        return '0' <= value <= '9'
