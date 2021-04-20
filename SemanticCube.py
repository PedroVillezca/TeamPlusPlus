from util.Enums import Type, Operator

type_count = len(Type)
operator_count = len(Operator)
semantic_cube = [[[None for k in range(operator_count)] for j in range(type_count)] for i in range(type_count)]

semantic_cube[Type.INT][Type.INT][Operator.OR] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.AND] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.EQ] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.GT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.LT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.GTE] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.LTE] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.DIFF] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.MULT] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.DIV] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.SUM] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.SUB] = Type.INT
semantic_cube[Type.INT][Type.INT][Operator.ASS] = Type.INT

semantic_cube[Type.INT][Type.FLOAT][Operator.OR] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.AND] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.EQ] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.GT] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.LT] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.GTE] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.LTE] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.DIFF] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.ASS] = Type.INT
semantic_cube[Type.INT][Type.FLOAT][Operator.MULT] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.DIV] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.SUM] = Type.FLOAT
semantic_cube[Type.INT][Type.FLOAT][Operator.SUB] = Type.FLOAT

semantic_cube[Type.FLOAT][Type.INT][Operator.OR] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.AND] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.EQ] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.GT] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.LT] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.GTE] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.LTE] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.DIFF] = Type.INT
semantic_cube[Type.FLOAT][Type.INT][Operator.MULT] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.DIV] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.SUM] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.SUB] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.INT][Operator.ASS] = Type.FLOAT

semantic_cube[Type.FLOAT][Type.FLOAT][Operator.OR] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.AND] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.EQ] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.GT] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.LT] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.GTE] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.LTE] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.DIFF] = Type.INT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.MULT] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.DIV] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.SUM] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.SUB] = Type.FLOAT
semantic_cube[Type.FLOAT][Type.FLOAT][Operator.ASS] = Type.FLOAT

semantic_cube[Type.CHAR][Type.CHAR][Operator.EQ] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.GT] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.LT] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.GTE] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.LTE] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.DIFF] = Type.INT
semantic_cube[Type.CHAR][Type.CHAR][Operator.ASS] = Type.CHAR