# 参考文档

https://crossoverjie.top/2020/03/23/compilation/Lexer/

# ANTLR

一个解析器生成器，用于读取处理结构化文本，常用于构建语言，工具和框架

### Install

```bash
pip install antlr4-tools
pip install antlr4-python3-runtime
# 安装 antlr4-tool 插件
```

### Example

```text
// 与文件同名 Calc.g4，该文件是一种上下文无关的文法表示
grammar Calc;	

// 程序 就是一个表达式然后结束，prog 为程序的入口，可以修改为其他名字
prog:	expr EOF ;

// 表达式可以使数字、括号、嵌套乘除或加减
// 注意#MulDiv这一部分不能忽略，他会作为一个生成程序时候对应的方法名
// 注意op=xxx这个写法本来可以直接写成('+'|'-')，但是这样很难维护
expr
    : expr op=(MUL|DIV) expr    # MulDiv
    | expr op=(ADD|SUB) expr    # AddSub
    | INT                       # Int
    | '(' expr ')'              # Parens
    ;
NEWLINE : [\r\n ]+ -> skip;
INT     : [0-9]+ ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
```
`antlr4 -Dlanguage=Python3 Hello.g4 -o code`

直接最左递归被允许，间接最左递归不被允许
