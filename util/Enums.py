from enum import IntEnum

class Type(IntEnum):
    INT = 0
    FLOAT = 1
    CHAR = 2
    VOID = 3
    ID = 4

class Level(IntEnum):
    PUBLIC = 0
    PRIVATE = 1

class Operator(IntEnum):
    OR = 0
    AND = 1
    EQ = 2
    GT = 3
    LT = 4
    GTE = 5
    LTE = 6
    DIFF = 7
    MULT = 8
    DIV = 9
    SUM = 10 
    SUB = 11
    POS = 12
    NEG = 13
    NOT = 14
    ASSIGN = 15
    FF = 16
    RETURN = 17
    READ = 18
    PRINT = 19
    GOTO = 20
    GOTOF = 21
    GOSUB = 22
    PARAMETER = 23
    ERA = 24
    ENDFUNC = 25
    GOMAIN = 26
    