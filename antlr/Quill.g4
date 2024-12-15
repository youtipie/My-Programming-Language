grammar Quill;

program
    : statementList EOF
    ;

statementList
    : (statement | COMMENT)*
    ;

statement
    : declaration (';' | NEWLINE)
    | assign (';' | NEWLINE)
    | ifStatement
    | forStatement
    | whileStatement
    | COMMENT
    | out (';' | NEWLINE)
    | NEWLINE
    ;

declaration
    : declarationKeyword ident declarationExpression (',' ident declarationExpression)*
    ;

ident
    : (LETTER | UNICODE_SYMBOL | '_') (LETTER | UNICODE_SYMBOL | DIGIT | '_')*
    ;

declarationExpression
    : ((':' type)? '=' (expression | inp))
    | ':' type
    ;

assign
    : ident '=' (expression | inp)
    ;

ifStatement
    : 'if' expression '{' statementList '}' ifTail?
    ;

ifTail
    : 'else' (('{' statementList '}') | ifStatement)
    ;

forStatement
    : 'for' ident 'in' rangeExpr '{' statementList '}'
    ;

rangeExpr
    : expression rangeOp expression
    ;

whileStatement
    : 'while' expression '{' statementList '}'
    ;

COMMENT
    : '//' ~('\n')* -> skip
    ;

inp
    : 'readLine()'
    ;

out
    : 'print' '(' expression (',' expression)* ')'
    ;

expression
    : arithmExpression (relOp arithmExpression)*
    ;

relOp
    : '==' | '<=' | '<' | '>' | '>=' | '!='
    ;

arithmExpression
    : sign? term (('+' | '-') term)*
    ;

term
    : exponent (('*' | '/') exponent)*
    ;

exponent
    : factor ('^' factor)*
    ;

factor
    : ident
    | constant
    | '(' expression ')'
    ;

constant
    : intNumb
    | floatNumb
    | boolConst
    ;

declarationKeyword
    : 'var' | 'let'
    ;

sign
    : '+' | '-'
    ;

type
    : 'Int' | 'Float' | 'Bool'
    ;

rangeOp
    : '...'
    | '..<'
    ;

intNumb
    : sign? unsignedInt
    ;

floatNumb
    : unsignedFloat '.' unsignedFloat
    ;

unsignedInt
    : DIGIT (DIGIT)*
    ;

unsignedFloat
    : unsignedInt '.' unsignedInt
    ;

boolConst
    : 'true' | 'false'
    ;

LETTER
    : [a-zA-Z]
    ;

UNICODE_SYMBOL
    : [\u0080-\uFFFF]
    ;

DIGIT
    : [0-9]
    ;

NEWLINE
    : [\n\r]
    ;

WS
    : [ \t]+ -> skip
    ;
