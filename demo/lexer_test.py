import unittest

from demo.consts import TokenType
from demo.lexer import TestLexer


class TestLexerTest(unittest.TestCase):

    def test_tokenize_1(self):
        lexer = TestLexer()
        script = "x = 100"
        tokens = lexer.tokenize(script)

        print("token\tvalue")
        for result in tokens:
            print(result.token_type, "\t", result.get_text())

        self.assertEqual(tokens[0].token_type, TokenType.VAR)
        self.assertEqual(tokens[0].get_text(), "x")

        self.assertEqual(tokens[1].token_type, TokenType.GE)
        self.assertEqual(tokens[1].get_text(), "=")

        self.assertEqual(tokens[2].token_type, TokenType.VAL)
        self.assertEqual(tokens[2].get_text(), "100")

    def test_tokenize_2(self):
        lexer = TestLexer()
        script = "ab = 10"
        tokens = lexer.tokenize(script)

        print("token\tvalue")
        for result in tokens:
            print(result.token_type, "\t", result.get_text())

        self.assertEqual(tokens[0].token_type, TokenType.VAR)
        self.assertEqual(tokens[0].get_text(), "ab")

        self.assertEqual(tokens[1].token_type, TokenType.GE)
        self.assertEqual(tokens[1].get_text(), "=")

        self.assertEqual(tokens[2].token_type, TokenType.VAL)
        self.assertEqual(tokens[2].get_text(), "10")


if __name__ == "__main__":
    unittest.main()
