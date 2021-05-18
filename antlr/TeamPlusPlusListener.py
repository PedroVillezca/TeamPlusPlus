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


    # Enter a parse tree produced by TeamPlusPlusParser#global_vars.
    def enterGlobal_vars(self, ctx:TeamPlusPlusParser.Global_varsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#global_vars.
    def exitGlobal_vars(self, ctx:TeamPlusPlusParser.Global_varsContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#attr_call.
    def enterAttr_call(self, ctx:TeamPlusPlusParser.Attr_callContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#attr_call.
    def exitAttr_call(self, ctx:TeamPlusPlusParser.Attr_callContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#attr.
    def enterAttr(self, ctx:TeamPlusPlusParser.AttrContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#attr.
    def exitAttr(self, ctx:TeamPlusPlusParser.AttrContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#init.
    def enterInit(self, ctx:TeamPlusPlusParser.InitContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#init.
    def exitInit(self, ctx:TeamPlusPlusParser.InitContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#init_arr.
    def enterInit_arr(self, ctx:TeamPlusPlusParser.Init_arrContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#init_arr.
    def exitInit_arr(self, ctx:TeamPlusPlusParser.Init_arrContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#first_dim.
    def enterFirst_dim(self, ctx:TeamPlusPlusParser.First_dimContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#first_dim.
    def exitFirst_dim(self, ctx:TeamPlusPlusParser.First_dimContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#second_dim.
    def enterSecond_dim(self, ctx:TeamPlusPlusParser.Second_dimContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#second_dim.
    def exitSecond_dim(self, ctx:TeamPlusPlusParser.Second_dimContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#init_assign.
    def enterInit_assign(self, ctx:TeamPlusPlusParser.Init_assignContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#init_assign.
    def exitInit_assign(self, ctx:TeamPlusPlusParser.Init_assignContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#functions.
    def enterFunctions(self, ctx:TeamPlusPlusParser.FunctionsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#functions.
    def exitFunctions(self, ctx:TeamPlusPlusParser.FunctionsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#c_functions.
    def enterC_functions(self, ctx:TeamPlusPlusParser.C_functionsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#c_functions.
    def exitC_functions(self, ctx:TeamPlusPlusParser.C_functionsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_function.
    def enterTpp_function(self, ctx:TeamPlusPlusParser.Tpp_functionContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_function.
    def exitTpp_function(self, ctx:TeamPlusPlusParser.Tpp_functionContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#declare_func.
    def enterDeclare_func(self, ctx:TeamPlusPlusParser.Declare_funcContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#declare_func.
    def exitDeclare_func(self, ctx:TeamPlusPlusParser.Declare_funcContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#return_type.
    def enterReturn_type(self, ctx:TeamPlusPlusParser.Return_typeContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#return_type.
    def exitReturn_type(self, ctx:TeamPlusPlusParser.Return_typeContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#void_type.
    def enterVoid_type(self, ctx:TeamPlusPlusParser.Void_typeContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#void_type.
    def exitVoid_type(self, ctx:TeamPlusPlusParser.Void_typeContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#params.
    def enterParams(self, ctx:TeamPlusPlusParser.ParamsContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#params.
    def exitParams(self, ctx:TeamPlusPlusParser.ParamsContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#param.
    def enterParam(self, ctx:TeamPlusPlusParser.ParamContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#param.
    def exitParam(self, ctx:TeamPlusPlusParser.ParamContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#assign_exp.
    def enterAssign_exp(self, ctx:TeamPlusPlusParser.Assign_expContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#assign_exp.
    def exitAssign_exp(self, ctx:TeamPlusPlusParser.Assign_expContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#assign_op.
    def enterAssign_op(self, ctx:TeamPlusPlusParser.Assign_opContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#assign_op.
    def exitAssign_op(self, ctx:TeamPlusPlusParser.Assign_opContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#funcall.
    def enterFuncall(self, ctx:TeamPlusPlusParser.FuncallContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#funcall.
    def exitFuncall(self, ctx:TeamPlusPlusParser.FuncallContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#argument.
    def enterArgument(self, ctx:TeamPlusPlusParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#argument.
    def exitArgument(self, ctx:TeamPlusPlusParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#func_name.
    def enterFunc_name(self, ctx:TeamPlusPlusParser.Func_nameContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#func_name.
    def exitFunc_name(self, ctx:TeamPlusPlusParser.Func_nameContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#method_call.
    def enterMethod_call(self, ctx:TeamPlusPlusParser.Method_callContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#method_call.
    def exitMethod_call(self, ctx:TeamPlusPlusParser.Method_callContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#read_var.
    def enterRead_var(self, ctx:TeamPlusPlusParser.Read_varContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#read_var.
    def exitRead_var(self, ctx:TeamPlusPlusParser.Read_varContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_print.
    def enterTpp_print(self, ctx:TeamPlusPlusParser.Tpp_printContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_print.
    def exitTpp_print(self, ctx:TeamPlusPlusParser.Tpp_printContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#print_val.
    def enterPrint_val(self, ctx:TeamPlusPlusParser.Print_valContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#print_val.
    def exitPrint_val(self, ctx:TeamPlusPlusParser.Print_valContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#print_exp.
    def enterPrint_exp(self, ctx:TeamPlusPlusParser.Print_expContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#print_exp.
    def exitPrint_exp(self, ctx:TeamPlusPlusParser.Print_expContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#print_string.
    def enterPrint_string(self, ctx:TeamPlusPlusParser.Print_stringContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#print_string.
    def exitPrint_string(self, ctx:TeamPlusPlusParser.Print_stringContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#if_expr.
    def enterIf_expr(self, ctx:TeamPlusPlusParser.If_exprContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#if_expr.
    def exitIf_expr(self, ctx:TeamPlusPlusParser.If_exprContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_elif.
    def enterTpp_elif(self, ctx:TeamPlusPlusParser.Tpp_elifContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_elif.
    def exitTpp_elif(self, ctx:TeamPlusPlusParser.Tpp_elifContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_else.
    def enterTpp_else(self, ctx:TeamPlusPlusParser.Tpp_elseContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_else.
    def exitTpp_else(self, ctx:TeamPlusPlusParser.Tpp_elseContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:TeamPlusPlusParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:TeamPlusPlusParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#switch_expr.
    def enterSwitch_expr(self, ctx:TeamPlusPlusParser.Switch_exprContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#switch_expr.
    def exitSwitch_expr(self, ctx:TeamPlusPlusParser.Switch_exprContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#cases.
    def enterCases(self, ctx:TeamPlusPlusParser.CasesContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#cases.
    def exitCases(self, ctx:TeamPlusPlusParser.CasesContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#next_case.
    def enterNext_case(self, ctx:TeamPlusPlusParser.Next_caseContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#next_case.
    def exitNext_case(self, ctx:TeamPlusPlusParser.Next_caseContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_case.
    def enterTpp_case(self, ctx:TeamPlusPlusParser.Tpp_caseContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_case.
    def exitTpp_case(self, ctx:TeamPlusPlusParser.Tpp_caseContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#switch_cte.
    def enterSwitch_cte(self, ctx:TeamPlusPlusParser.Switch_cteContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#switch_cte.
    def exitSwitch_cte(self, ctx:TeamPlusPlusParser.Switch_cteContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#switch_block.
    def enterSwitch_block(self, ctx:TeamPlusPlusParser.Switch_blockContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#switch_block.
    def exitSwitch_block(self, ctx:TeamPlusPlusParser.Switch_blockContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#tpp_default.
    def enterTpp_default(self, ctx:TeamPlusPlusParser.Tpp_defaultContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#tpp_default.
    def exitTpp_default(self, ctx:TeamPlusPlusParser.Tpp_defaultContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#while_expr.
    def enterWhile_expr(self, ctx:TeamPlusPlusParser.While_exprContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#while_expr.
    def exitWhile_expr(self, ctx:TeamPlusPlusParser.While_exprContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#floop.
    def enterFloop(self, ctx:TeamPlusPlusParser.FloopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#floop.
    def exitFloop(self, ctx:TeamPlusPlusParser.FloopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#for_assign.
    def enterFor_assign(self, ctx:TeamPlusPlusParser.For_assignContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#for_assign.
    def exitFor_assign(self, ctx:TeamPlusPlusParser.For_assignContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#for_var.
    def enterFor_var(self, ctx:TeamPlusPlusParser.For_varContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#for_var.
    def exitFor_var(self, ctx:TeamPlusPlusParser.For_varContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#for_to.
    def enterFor_to(self, ctx:TeamPlusPlusParser.For_toContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#for_to.
    def exitFor_to(self, ctx:TeamPlusPlusParser.For_toContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#expression.
    def enterExpression(self, ctx:TeamPlusPlusParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#expression.
    def exitExpression(self, ctx:TeamPlusPlusParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#orop.
    def enterOrop(self, ctx:TeamPlusPlusParser.OropContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#orop.
    def exitOrop(self, ctx:TeamPlusPlusParser.OropContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#expressio.
    def enterExpressio(self, ctx:TeamPlusPlusParser.ExpressioContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#expressio.
    def exitExpressio(self, ctx:TeamPlusPlusParser.ExpressioContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#andop.
    def enterAndop(self, ctx:TeamPlusPlusParser.AndopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#andop.
    def exitAndop(self, ctx:TeamPlusPlusParser.AndopContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#express.
    def enterExpress(self, ctx:TeamPlusPlusParser.ExpressContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#express.
    def exitExpress(self, ctx:TeamPlusPlusParser.ExpressContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#rel_exp.
    def enterRel_exp(self, ctx:TeamPlusPlusParser.Rel_expContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#rel_exp.
    def exitRel_exp(self, ctx:TeamPlusPlusParser.Rel_expContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#factor_elem.
    def enterFactor_elem(self, ctx:TeamPlusPlusParser.Factor_elemContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#factor_elem.
    def exitFactor_elem(self, ctx:TeamPlusPlusParser.Factor_elemContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#fake_bottom.
    def enterFake_bottom(self, ctx:TeamPlusPlusParser.Fake_bottomContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#fake_bottom.
    def exitFake_bottom(self, ctx:TeamPlusPlusParser.Fake_bottomContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#unop.
    def enterUnop(self, ctx:TeamPlusPlusParser.UnopContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#unop.
    def exitUnop(self, ctx:TeamPlusPlusParser.UnopContext):
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


    # Enter a parse tree produced by TeamPlusPlusParser#val_var.
    def enterVal_var(self, ctx:TeamPlusPlusParser.Val_varContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#val_var.
    def exitVal_var(self, ctx:TeamPlusPlusParser.Val_varContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#val_cte.
    def enterVal_cte(self, ctx:TeamPlusPlusParser.Val_cteContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#val_cte.
    def exitVal_cte(self, ctx:TeamPlusPlusParser.Val_cteContext):
        pass


    # Enter a parse tree produced by TeamPlusPlusParser#val_funcall.
    def enterVal_funcall(self, ctx:TeamPlusPlusParser.Val_funcallContext):
        pass

    # Exit a parse tree produced by TeamPlusPlusParser#val_funcall.
    def exitVal_funcall(self, ctx:TeamPlusPlusParser.Val_funcallContext):
        pass



del TeamPlusPlusParser