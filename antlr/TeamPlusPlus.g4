grammar TeamPlusPlus;

// Parser Rules
program     : PROGRAM ID SEMICOLON imports? classes? tpp_vars? functions? main EOF;

imports     : (IMPORT ID SEMICOLON)+;

classes     : (tpp_class)+;

tpp_class   : CLASS ID (inherit)? LEFT_BRACE c_vars? c_functions? RIGHT_BRACE SEMICOLON;

inherit     : INHERITS ID;

tpp_vars    : VARS ((id_type | tpp_type) init (COMMA init)* SEMICOLON)+;

id_type     : ID;

c_vars      : ATTRIBUTES (level (id_type | tpp_type) init (COMMA init)* SEMICOLON)+;

var         : ID (LEFT_BRACKET exp (COMMA exp)? RIGHT_BRACKET)? (attr_call)?;

attr_call   : DOT attr;

attr        : ID (LEFT_BRACKET exp (COMMA exp)? RIGHT_BRACKET)? (attr_call)?;

init        : ID (LEFT_BRACKET CTE_INT (COMMA CTE_INT)? RIGHT_BRACKET)? init_assign;

init_assign : (assign_exp)?;

functions   : (FUNC declare_func LEFT_PARENTHESIS (param (COMMA param)*)? RIGHT_PARENTHESIS funblock)+;

declare_func: (void_type | tpp_type) ID;

param       : (tpp_type | id_type) ID;

void_type   : VOID;

c_functions : METHODS (level FUNC declare_func LEFT_PARENTHESIS (param (COMMA param)*)? RIGHT_PARENTHESIS funblock)+;

main        : MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS funblock;

funblock    : LEFT_BRACE tpp_vars? statement* RIGHT_BRACE;

tpp_type    : (INT | FLOAT | CHAR);

level       : (PUBLIC | PRIVATE);

statement   : (assignment | funcall SEMICOLON | read | tpp_return | tpp_print | condition | loop);

assignment  : var assign_exp SEMICOLON;

assign_exp  : assign_op expression;

assign_op   : ASSIGN;

funcall     : (method_call)? func_name LEFT_PARENTHESIS (expression (COMMA expression)*)? RIGHT_PARENTHESIS;

func_name   : ID;

method_call : var DOT;

tpp_return  : RETURN LEFT_PARENTHESIS exp RIGHT_PARENTHESIS SEMICOLON;

read        : READ LEFT_PARENTHESIS read_var (COMMA read_var)* RIGHT_PARENTHESIS SEMICOLON;

read_var    : var;

tpp_print   : PRINT LEFT_PARENTHESIS print_val (COMMA print_val)* RIGHT_PARENTHESIS SEMICOLON;

print_val   : (print_exp | print_string);

print_exp   : expression;

print_string: CTE_STRING;

block       : LEFT_BRACE statement* RIGHT_BRACE;

condition   : (ifelse | switch_stmt);

ifelse      : IF if_expr block (tpp_elif)* (tpp_else)?;

if_expr     : LEFT_PARENTHESIS expression RIGHT_PARENTHESIS;

tpp_elif    : ELIF if_expr block;

tpp_else    : ELSE block;

switch_stmt : SWITCH switch_var LEFT_BRACE cases (tpp_default)?  RIGHT_BRACE;

switch_var  : LEFT_PARENTHESIS var RIGHT_PARENTHESIS;

cases       : tpp_case (next_case)*;

next_case   : tpp_case;

tpp_case    : CASE switch_cte switch_block;

switch_cte  : (CTE_CHAR | CTE_INT);

switch_block: block;

tpp_default : DEFAULT block;

loop        : (wloop | floop);

wloop       : WHILE while_expr block;

while_expr  : LEFT_PARENTHESIS expression RIGHT_PARENTHESIS;

floop       : FROM for_assign for_to block;

for_assign  : for_var ASSIGN exp;

for_var     : var;

for_to      : TO exp;

expression  : expressio (orop expressio)*;

orop        : OR;

expressio   : express (andop express)*;

andop       : AND;

express     : exp (relop rel_exp)?;

rel_exp     : exp;

exp         : term (sumop term)*;

term        : factor (mulop factor)*;

factor      : unop? factor_elem;

factor_elem : (fake_bottom | value);

fake_bottom : LEFT_PARENTHESIS expression RIGHT_PARENTHESIS;

unop        : (PLUS | MINUS | NOT);

relop       : (EQUALS | GREATER_THAN | LESS_THAN | GREATER_EQUALS | LESS_EQUALS | DIFFERENT);

sumop       : (PLUS | MINUS);

mulop       : (MULT | DIV);

value       : (val_var | val_cte | val_funcall);

val_var     : var;

val_cte     : CTE_INT | CTE_FLOAT | CTE_CHAR;

val_funcall : funcall;

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