# Generated from TeamPlusPlus.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TeamPlusPlusParser import TeamPlusPlusParser
else:
    from TeamPlusPlusParser import TeamPlusPlusParser

# This class defines a complete listener for a parse tree produced by TeamPlusPlusParser.
class TeamPlusPlusListener(ParseTreeListener):

    # Enter a parse tree produced by TeamPlusPlusParser#program.
    def enterProgram(self, ctx:TeamPlusPlusParser.ProgramContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#program.
    def exitProgram(self, ctx:TeamPlusPlusParser.ProgramContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#imports.
    def enterImports(self, ctx:TeamPlusPlusParser.ImportsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#imports.
    def exitImports(self, ctx:TeamPlusPlusParser.ImportsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#classes.
    def enterClasses(self, ctx:TeamPlusPlusParser.ClassesContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#classes.
    def exitClasses(self, ctx:TeamPlusPlusParser.ClassesContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_class.
    def enterTpp_class(self, ctx:TeamPlusPlusParser.Tpp_classContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_class.
    def exitTpp_class(self, ctx:TeamPlusPlusParser.Tpp_classContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#inherit.
    def enterInherit(self, ctx:TeamPlusPlusParser.InheritContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#inherit.
    def exitInherit(self, ctx:TeamPlusPlusParser.InheritContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_vars.
    def enterTpp_vars(self, ctx:TeamPlusPlusParser.Tpp_varsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_vars.
    def exitTpp_vars(self, ctx:TeamPlusPlusParser.Tpp_varsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#id_type.
    def enterId_type(self, ctx:TeamPlusPlusParser.Id_typeContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#id_type.
    def exitId_type(self, ctx:TeamPlusPlusParser.Id_typeContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#c_vars.
    def enterC_vars(self, ctx:TeamPlusPlusParser.C_varsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#c_vars.
    def exitC_vars(self, ctx:TeamPlusPlusParser.C_varsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#var.
    def enterVar(self, ctx:TeamPlusPlusParser.VarContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#var.
    def exitVar(self, ctx:TeamPlusPlusParser.VarContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#init.
    def enterInit(self, ctx:TeamPlusPlusParser.InitContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#init.
    def exitInit(self, ctx:TeamPlusPlusParser.InitContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#functions.
    def enterFunctions(self, ctx:TeamPlusPlusParser.FunctionsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#functions.
    def exitFunctions(self, ctx:TeamPlusPlusParser.FunctionsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#declare_func.
    def enterDeclare_func(self, ctx:TeamPlusPlusParser.Declare_funcContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#declare_func.
    def exitDeclare_func(self, ctx:TeamPlusPlusParser.Declare_funcContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#param.
    def enterParam(self, ctx:TeamPlusPlusParser.ParamContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#param.
    def exitParam(self, ctx:TeamPlusPlusParser.ParamContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#void_type.
    def enterVoid_type(self, ctx:TeamPlusPlusParser.Void_typeContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#void_type.
    def exitVoid_type(self, ctx:TeamPlusPlusParser.Void_typeContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#c_functions.
    def enterC_functions(self, ctx:TeamPlusPlusParser.C_functionsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#c_functions.
    def exitC_functions(self, ctx:TeamPlusPlusParser.C_functionsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#main.
    def enterMain(self, ctx:TeamPlusPlusParser.MainContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#main.
    def exitMain(self, ctx:TeamPlusPlusParser.MainContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#funblock.
    def enterFunblock(self, ctx:TeamPlusPlusParser.FunblockContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#funblock.
    def exitFunblock(self, ctx:TeamPlusPlusParser.FunblockContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_type.
    def enterTpp_type(self, ctx:TeamPlusPlusParser.Tpp_typeContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_type.
    def exitTpp_type(self, ctx:TeamPlusPlusParser.Tpp_typeContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#level.
    def enterLevel(self, ctx:TeamPlusPlusParser.LevelContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#level.
    def exitLevel(self, ctx:TeamPlusPlusParser.LevelContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#statement.
    def enterStatement(self, ctx:TeamPlusPlusParser.StatementContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#statement.
    def exitStatement(self, ctx:TeamPlusPlusParser.StatementContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#assignment.
    def enterAssignment(self, ctx:TeamPlusPlusParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#assignment.
    def exitAssignment(self, ctx:TeamPlusPlusParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#funcall.
    def enterFuncall(self, ctx:TeamPlusPlusParser.FuncallContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#funcall.
    def exitFuncall(self, ctx:TeamPlusPlusParser.FuncallContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_return.
    def enterTpp_return(self, ctx:TeamPlusPlusParser.Tpp_returnContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_return.
    def exitTpp_return(self, ctx:TeamPlusPlusParser.Tpp_returnContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#read.
    def enterRead(self, ctx:TeamPlusPlusParser.ReadContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#read.
    def exitRead(self, ctx:TeamPlusPlusParser.ReadContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_print.
    def enterTpp_print(self, ctx:TeamPlusPlusParser.Tpp_printContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_print.
    def exitTpp_print(self, ctx:TeamPlusPlusParser.Tpp_printContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#block.
    def enterBlock(self, ctx:TeamPlusPlusParser.BlockContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#block.
    def exitBlock(self, ctx:TeamPlusPlusParser.BlockContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#condition.
    def enterCondition(self, ctx:TeamPlusPlusParser.ConditionContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#condition.
    def exitCondition(self, ctx:TeamPlusPlusParser.ConditionContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#ifelse.
    def enterIfelse(self, ctx:TeamPlusPlusParser.IfelseContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#ifelse.
    def exitIfelse(self, ctx:TeamPlusPlusParser.IfelseContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:TeamPlusPlusParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:TeamPlusPlusParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#loop.
    def enterLoop(self, ctx:TeamPlusPlusParser.LoopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#loop.
    def exitLoop(self, ctx:TeamPlusPlusParser.LoopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#wloop.
    def enterWloop(self, ctx:TeamPlusPlusParser.WloopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#wloop.
    def exitWloop(self, ctx:TeamPlusPlusParser.WloopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#floop.
    def enterFloop(self, ctx:TeamPlusPlusParser.FloopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#floop.
    def exitFloop(self, ctx:TeamPlusPlusParser.FloopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#expression.
    def enterExpression(self, ctx:TeamPlusPlusParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#expression.
    def exitExpression(self, ctx:TeamPlusPlusParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#expression_A.
    def enterExpression_A(self, ctx:TeamPlusPlusParser.Expression_AContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#expression_A.
    def exitExpression_A(self, ctx:TeamPlusPlusParser.Expression_AContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#express.
    def enterExpress(self, ctx:TeamPlusPlusParser.ExpressContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#express.
    def exitExpress(self, ctx:TeamPlusPlusParser.ExpressContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#exp.
    def enterExp(self, ctx:TeamPlusPlusParser.ExpContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#exp.
    def exitExp(self, ctx:TeamPlusPlusParser.ExpContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#term.
    def enterTerm(self, ctx:TeamPlusPlusParser.TermContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#term.
    def exitTerm(self, ctx:TeamPlusPlusParser.TermContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#factor.
    def enterFactor(self, ctx:TeamPlusPlusParser.FactorContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#factor.
    def exitFactor(self, ctx:TeamPlusPlusParser.FactorContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#relop.
    def enterRelop(self, ctx:TeamPlusPlusParser.RelopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#relop.
    def exitRelop(self, ctx:TeamPlusPlusParser.RelopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#sumop.
    def enterSumop(self, ctx:TeamPlusPlusParser.SumopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#sumop.
    def exitSumop(self, ctx:TeamPlusPlusParser.SumopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#mulop.
    def enterMulop(self, ctx:TeamPlusPlusParser.MulopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#mulop.
    def exitMulop(self, ctx:TeamPlusPlusParser.MulopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#value.
    def enterValue(self, ctx:TeamPlusPlusParser.ValueContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#value.
    def exitValue(self, ctx:TeamPlusPlusParser.ValueContext):
        pass



del TeamPlusPlusParser