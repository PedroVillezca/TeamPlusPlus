grammar TeamPlusPlus;

// Parser Rules
program     : PROGRAM ID SEMICOLON imports? classes? tpp_vars? functions? main EOF;

imports     : (IMPORT ID SEMICOLON)+;

classes     : (tpp_class)+;

tpp_class   : CLASS ID (inherit)? LEFT_BRACE c_vars? c_functions? RIGHT_BRACE SEMICOLON;

inherit     : INHERITS ID;

tpp_vars    : VARS ((id_type | tpp_type) init (COMMA init)* SEMICOLON)+;

id_type     : ID;

c_vars      : ATTRIBUTES (level? (id_type | tpp_type) init (COMMA init)* SEMICOLON)+;

var         : ID (LEFT_BRACKET exp (COMMA exp)? RIGHT_BRACKET)? (DOT var)?;

init        : ID (LEFT_BRACKET CTE_INT (COMMA CTE_INT)? RIGHT_BRACKET)? (ASSIGN expression)?;

functions   : (FUNC declare_func LEFT_PARENTHESIS (param (COMMA param)*)? RIGHT_PARENTHESIS funblock)+;

declare_func: (void_type | tpp_type) ID;

param       : (tpp_type | id_type) ID;

void_type   : VOID;

c_functions : METHODS (level? FUNC declare_func LEFT_PARENTHESIS (param (COMMA param)*)? RIGHT_PARENTHESIS funblock)+;

main        : MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS funblock;

funblock    : LEFT_BRACE tpp_vars? statement* RIGHT_BRACE;

tpp_type    : (INT | FLOAT | CHAR);

level       : (PUBLIC | PRIVATE);

statement   : (assignment | funcall SEMICOLON | tpp_return | read | tpp_print | condition | loop);

assignment  : var ASSIGN expression SEMICOLON;

funcall     : (var DOT)? ID LEFT_PARENTHESIS (expression (COMMA expression)*)? RIGHT_PARENTHESIS;

tpp_return  : RETURN LEFT_PARENTHESIS exp RIGHT_PARENTHESIS SEMICOLON;

read        : READ LEFT_PARENTHESIS var (COMMA var)* RIGHT_PARENTHESIS SEMICOLON;

tpp_print   : PRINT LEFT_PARENTHESIS (expression | CTE_STRING) (COMMA (expression | CTE_STRING))* RIGHT_PARENTHESIS SEMICOLON;

block       : LEFT_BRACE statement* RIGHT_BRACE;

condition   : (ifelse | switch_stmt);

ifelse      : IF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS THEN block (ELIF LEFT_PARENTHESIS expression RIGHT_PARENTHESIS THEN block)* (ELSE block)?;

switch_stmt : SWITCH LEFT_PARENTHESIS var RIGHT_PARENTHESIS LEFT_BRACE (CASE (CTE_CHAR | CTE_INT) block)* (DEFAULT block)?  RIGHT_BRACE;

loop        : (wloop | floop);

wloop       : WHILE LEFT_PARENTHESIS expression RIGHT_PARENTHESIS block;

floop       : FROM var ASSIGN exp TO exp block;

expression  : express expression_A | NOT expression expression_A;

expression_A: ((AND | OR) expression expression_A)?;

express     : exp (relop exp)?;

exp         : term (sumop term)*;

term        : factor (mulop factor)*;

factor      : (LEFT_PARENTHESIS expression RIGHT_PARENTHESIS | sumop? value);

relop       : (EQUALS | GREATER_THAN | LESS_THAN | GREATER_EQUALS | LESS_EQUALS | DIFFERENT);

sumop       : (PLUS | MINUS);

mulop       : (MULT | DIV);

value       : (var | CTE_INT | CTE_FLOAT | CTE_CHAR | funcall);

// Regular Definition
PROGRAM     : 'program';
INT         : 'int';
FLOAT       : 'float';
CHAR        : 'char';
VARS        : 'vars';
CLASS       : 'class';
INHERITS    : 'inherits';
MAIN        : 'main';
IF          : 'if';
ELSE        : 'else';
ELIF        : 'elif';
THEN        : 'then';
SWITCH      : 'switch';
CASE        : 'case';
DEFAULT     : 'default';
FUNC        : 'func';
RETURN      : 'return';
READ        : 'read';
PRINT       : 'print';
WHILE       : 'while';
FROM        : 'from';
TO          : 'to';
ATTRIBUTES  : 'attributes';
METHODS     : 'methods';
IMPORT      : 'import';
AS          : 'as';
PUBLIC      : 'public';
PRIVATE     : 'private';
AND         : 'and';
OR          : 'or';
NOT         : 'not';
VOID        : 'void';

COLON               : ':';
COMMA               : ',';
DOT                 : '.';
ASSIGN              : '=';
LEFT_BRACE          : '{';
RIGHT_BRACE         : '}';
LEFT_PARENTHESIS    : '(';
RIGHT_PARENTHESIS   : ')';
LEFT_BRACKET        : '[';
RIGHT_BRACKET       : ']';
SEMICOLON           : ';';
PLUS                : '+';
MINUS               : '-';
MULT                : '*';
DIV                 : '/';
EQUALS              : '==';
GREATER_THAN        : '>';
LESS_THAN           : '<';
GREATER_EQUALS      : '>=';
LESS_EQUALS         : '<=';
DIFFERENT           : '!=';

CTE_INT     : [0-9]+;
CTE_FLOAT   : CTE_INT ('.' CTE_INT)?;
CTE_CHAR    : '\''.'\'';
CTE_STRING  : '"'.*?'"';
ID          : [a-zA-Z]+[a-zA-Z0-9_]*;
COMMENT     : '#'.*?'\n' -> skip;
WHITESPACE: [ \r\n\t]+ -> skip;