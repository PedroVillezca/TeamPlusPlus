grammar TeamPlusPlus;

// Parser Rules
program     : PROGRAM ID SEMICOLON classes? global_vars functions? main EOF;

global_vars : tpp_vars?;

classes     : (tpp_class)+;

tpp_class   : CLASS ID (inherit)? LEFT_BRACE c_vars? c_functions? RIGHT_BRACE SEMICOLON;

inherit     : INHERITS ID;

tpp_vars    : VARS ((id_type | tpp_type) init (COMMA init)* SEMICOLON)+;

id_type     : ID;

c_vars      : ATTRIBUTES (level tpp_type c_init (COMMA c_init)* SEMICOLON)+;

var         : ID indexing? (DOT attr)?;

indexing    : LEFT_BRACKET first_index (COMMA second_index)? RIGHT_BRACKET;

first_index : expression;

second_index: expression;

attr        : ID indexing?;

init        : ID init_arr init_assign;

c_init      : ID init_arr;

init_arr    : (LEFT_BRACKET first_dim (COMMA second_dim)? RIGHT_BRACKET)?;

first_dim   : CTE_INT;

second_dim  : CTE_INT;

init_assign : (init_verify)?;

init_verify : assign_exp;

functions   : (tpp_function)+;

c_functions : METHODS (level tpp_function)+;

tpp_function: FUNC declare_func params funblock;

declare_func: return_type ID;

return_type : (void_type | tpp_type);

void_type   : VOID;

params      : LEFT_PARENTHESIS (param (COMMA param)*)? RIGHT_PARENTHESIS;

param       : tpp_type ID;

main        : MAIN LEFT_PARENTHESIS RIGHT_PARENTHESIS funblock;

funblock    : LEFT_BRACE tpp_vars? statement* RIGHT_BRACE;

tpp_type    : (INT | FLOAT | CHAR);

level       : (PUBLIC | PRIVATE);

statement   : (assignment | funcall SEMICOLON | read | tpp_return | tpp_print | condition | loop);

assignment  : var assign_exp SEMICOLON;

assign_exp  : assign_op expression;

assign_op   : ASSIGN;

funcall     : (method_call)? func_name LEFT_PARENTHESIS (argument (COMMA argument)*)? RIGHT_PARENTHESIS;

argument    : expression;

func_name   : ID;

method_call : var DOT;

tpp_return  : RETURN LEFT_PARENTHESIS expression RIGHT_PARENTHESIS SEMICOLON;

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

switch_stmt : SWITCH switch_expr LEFT_BRACE cases (tpp_default)?  RIGHT_BRACE;

switch_expr  : LEFT_PARENTHESIS expression RIGHT_PARENTHESIS;

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