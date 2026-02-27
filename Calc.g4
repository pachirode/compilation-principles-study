// 与文件同名
grammar Calc;

// 程序 就是一个表达式然后结束
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

// 大写字母是词法分析的 Token
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';