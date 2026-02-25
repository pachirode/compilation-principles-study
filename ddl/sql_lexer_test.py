import unittest

from ddl.sql_lexer import SqlLexer


class SqlLexerTest(unittest.TestCase):

    def test_tokenize_1(self):
        lexer = SqlLexer()
        sql = (
            "CREATE TABLE `P` (\n"
            "`id` int(11) NOT NULL AUTO_INCREMENT,\n"
            "PRIMARY KEY (`id`)\n"
            ")\n"
            "COMMENT = '默认配送费表';"
        )

        tokenize = lexer.tokenize(sql)
        for result in tokenize:
            print(f"{result.token_type}\t{str(result)}")

    def test_tokenize_2(self):
        lexer = SqlLexer()
        sql = (
            "CREATE TABLE `open_api_terminal_info` (\n"
            "  `name` varchar(50, 10) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '终端机名称',\n"
            "  PRIMARY KEY (`id`)\n"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 "
            "COLLATE=utf8mb4_unicode_ci COMMENT='商家终端机信息表'"
        )

        tokenize = lexer.tokenize(sql)
        for result in tokenize:
            print(f"{result.token_type}\t{str(result)}")

    def test_tokenize_3(self):
        lexer = SqlLexer()
        sql = "PRIMARY KEY (`id`)"
        tokenize = lexer.tokenize(sql)

        for result in tokenize:
            print(f"{result.token_type}\t{str(result)}")

    def test_tokenize_4(self):
        lexer = SqlLexer()
        sql = "(`id`)"
        tokenize = lexer.tokenize(sql)

        for result in tokenize:
            print(f"{result.token_type}\t{str(result)}")

    def test_tokenize_5(self):
        lexer = SqlLexer()
        sql = "`id`"
        tokenize = lexer.tokenize(sql)

        for result in tokenize:
            print(f"{result.token_type}\t{str(result)}")

    def test_tokenize_6(self):
        lexer = SqlLexer()
        sql = "`name` varchar(50),"
        tokenize = lexer.tokenize(sql)

        for result in tokenize:
            print(f"{result.token_type}\t{str(result)}")


if __name__ == "__main__":
    unittest.main()
