from antlr4 import *
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

from src.DirGen import DirGen
from src.QuadrupleList import QuadrupleList, Operand
from util.Enums import Operator, Type, Level
from util.SemanticCube import semantic_cube
from util.DataStructures import Stack

class CustomListener(TeamPlusPlusListener):
    dir_gen = DirGen()
    quadruple_list = QuadrupleList()
    temp_ints = [f'ti{i}' for i in range(100)]
    temp_floats = [f'tf{i}' for i in range(100)]
    temp_chars = [f'tc{i}' for i in range(100)]

    current_type = None
    current_type_id = None
    is_attribute = False
    caller_name = ""
    recurrent_vars = Stack()

    return_state = 0
    called_function_name = ""
    p_funcalls = Stack()


    def __repr__(self):
        return f'\nDir Gen: \n {self.dir_gen} \n\n Quadruple List: \n {self.quadruple_list}'

    def get_temp(self, result_type):
        # Add temp var to current function depending on type
        self.dir_gen.add_temp_var(result_type)

        if result_type == Type.INT:
            return self.temp_ints.pop(0)
        elif result_type == Type.FLOAT:
            return self.temp_floats.pop(0)
        elif result_type == Type.CHAR:
            return self.temp_chars.pop(0)
        else:
            return None

    def generate_quadruple(self, top_operator):
        right_operand = self.quadruple_list.pop_operand()
        left_operand = self.quadruple_list.pop_operand()
        result_type = semantic_cube[left_operand.variable_type][right_operand.variable_type][top_operator]

        if result_type is None:
            raise Exception(f"Invalid operand types \'{Type(left_operand.variable_type).name}\' and \'{Type(right_operand.variable_type).name}\' for operator {Operator(self.quadruple_list.top_operator()).name}.")
        
        result_name = self.get_temp(result_type)
        
        self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), left_operand.variable_name, right_operand.variable_name, result_name)
        self.quadruple_list.push_operand(result_name, result_type)
    
    def create_gotof(self):
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count)
        left_operand = self.quadruple_list.pop_operand()
        if left_operand.variable_type != Type.INT:
            raise Exception(f"Cannot evaluate value of type {Type(left_operand.variable_type).name} for conditions.")
        
        self.quadruple_list.push_quadruple(Operator.GOTOF, left_operand.variable_name, None, None)
    
    def create_cond_goto(self):
        self.quadruple_list.push_quadruple(Operator.GOTO, None, None, None)
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count - 1)

    def create_loop_goto(self):
        self.quadruple_list.push_quadruple(Operator.GOTO, None, None, None)
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(self.quadruple_list.quadruple_count-1, index)
        
    
    def empty_jumps(self):
        while self.quadruple_list.top_jump() != Operator.FF:
            index = self.quadruple_list.pop_jump()
            self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        self.quadruple_list.pop_jump()

    # Point 1
    def enterProgram(self, ctx):
        self.dir_gen.enterProgram(ctx)

    # Point 2
    def enterTpp_class(self, ctx):
        self.dir_gen.enterTpp_class(ctx)
        
    # Point 3
    def exitInherit(self, ctx):
        self.dir_gen.exitInherit(ctx)

    # Point 4
    def exitLevel(self, ctx):
        self.dir_gen.exitLevel(ctx)
        
    # Point 5
    def exitTpp_type(self, ctx):
        self.dir_gen.exitTpp_type(ctx)
        
    # Point 5
    def exitVoid_type(self, ctx):
        self.dir_gen.exitVoid_type(ctx)

    # Point 6
    def exitId_type(self, ctx):
        self.dir_gen.exitId_type(ctx)

    # Point 8
    def exitDeclare_func(self, ctx):
        self.dir_gen.exitDeclare_func(ctx)
        
    # Point 9 
    def enterClasses(self, ctx):
        self.dir_gen.enterClasses(ctx)
    
    # Point 10
    def enterMain(self, ctx):
        self.dir_gen.enterMain(ctx)
        
    # Point 11
    def exitClasses(self, ctx):
        self.dir_gen.exitClasses(ctx)
    
    # Point 12
    def enterDeclare_func(self, ctx):
        self.dir_gen.enterDeclare_func(ctx)
    
    # Point 13
    def exitFunblock(self, ctx):
        self.dir_gen.exitFunblock(ctx)
    
    # Point 14
    def enterVar(self, ctx):
        var_name = ctx.ID().getText()

        var_obj = self.dir_gen.variable_search(var_name, self.dir_gen.current_class)

        if var_obj is None:
            raise Exception(f"Variable \'{var_name}\' does not exist.")
        
        if var_obj.level == Level.PRIVATE and var_obj.original_class != self.dir_gen.current_class:
            raise Exception(f"Variable \'{var_name}\' is private to class {var_obj.original_class}.")
        
        self.current_type = var_obj.type
        if var_obj.type == Type.ID:
            self.current_type_id = var_obj.type_id
        self.caller_name = var_name

    # Point 20
    def exitVar(self, ctx):
        self.is_attribute = False

    # Point 60
    def enterAttr(self, ctx):
        var_name = ctx.ID().getText()
        var_obj = self.dir_gen.attribute_search(var_name, self.current_type_id)

        if var_obj is None:
            raise Exception(f"Variable \'{var_name}\' does not exist.")
        
        if var_obj.level == Level.PRIVATE and var_obj.original_class != self.dir_gen.current_class:
            raise Exception(f"Variable \'{var_name}\' is private to class {var_obj.original_class}.")
        
        self.current_type = var_obj.type
        if var_obj.type == Type.ID:
            self.current_type_id = var_obj.type_id
        self.caller_name += var_name
        
    # Point 15
    def enterAttr_call(self, ctx):
        self.is_attribute = True
        self.caller_name += '.'

    # Point 15
    def exitMethod_call(self, ctx):
        self.is_attribute = True
        self.caller_name += '.'
    
    # Point 16
    def exitVal_var(self, ctx):
        self.quadruple_list.push_operand(self.caller_name, self.current_type, self.current_type_id)

    # Point 17
    def exitVal_cte(self, ctx):
        if ctx.CTE_INT() is not None:
            self.quadruple_list.push_operand(self.temp_ints.pop(0), Type.INT)
        elif ctx.CTE_FLOAT() is not None:
            self.quadruple_list.push_operand(self.temp_floats.pop(0), Type.FLOAT)
        elif ctx.CTE_CHAR() is not None:
            self.quadruple_list.push_operand(self.temp_chars.pop(0), Type.CHAR)
        else:
            raise Exception(f"There are no class constants.")
        
    # Point 18
    def enterFunc_name(self, ctx):
        func_name = ctx.ID().getText()

        if self.is_attribute:
            func_obj = self.dir_gen.method_search(func_name, self.current_type_id)
        else:
            func_obj = self.dir_gen.function_search(func_name, self.dir_gen.current_class)

        if func_obj is None:
            raise Exception(f"Function \'{func_name}\' does not exist.")
        
        if func_obj.level == Level.PRIVATE and func_obj.original_class != self.dir_gen.current_class:
            raise Exception(f"Function \'{func_name}\' is private to class {func_obj.original_class}.")
        
        self.current_type = func_obj.return_type
        self.called_function = func_name
        
    # Point 19
    def exitVal_funcall(self, ctx):
        temp = self.get_temp(self.current_type)
        if temp is None:
            raise Exception(f"Functions must return primitive types when used in expressions.")

        self.quadruple_list.push_operand(temp, self.current_type)
        
    # Point 21
    def exitUnop(self, ctx):
        if ctx.PLUS() is not None:
            self.quadruple_list.push_operator(Operator.POS)
        elif ctx.MINUS() is not None:
            self.quadruple_list.push_operator(Operator.NEG)
        elif ctx.NOT() is not None:
            self.quadruple_list.push_operator(Operator.NOT)
        else:
            raise Exception(f"Invalid unary operator.")
        
    # Point 22
    def exitFactor_elem(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.POS or top_operator == Operator.NEG or top_operator == Operator.NOT:
            left_operand = self.quadruple_list.pop_operand()
        
            if left_operand.variable_type != Type.INT and left_operand.variable_type != Type.FLOAT:
                raise Exception(f"Invalid operand type \'{Type(left_operand.variable_type).name}\' for operator {Operator(self.quadruple_list.top_operator()).name}.")
        
            if left_operand.variable_type == Type.INT or top_operator == Operator.NOT:
                result_name = self.temp_ints.pop(0)
                result_type = Type.INT
            else:
                result_name = self.temp_floats.pop(0)
                result_type = Type.FLOAT

            self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), left_operand.variable_name, None, result_name)
            self.quadruple_list.push_operand(result_name, result_type)
        
    # Point 23
    def enterFake_bottom(self, ctx):
        self.quadruple_list.push_operator(Operator.FF)
        
    # Point 24
    def exitFake_bottom(self, ctx):
        if self.quadruple_list.top_operator() != Operator.FF:
            raise Exception(f'Unexpected missing fake bottom.')
        self.quadruple_list.pop_operator()
        
    # Point 25
    def exitMulop(self, ctx):
        if ctx.MULT() is not None:
            self.quadruple_list.push_operator(Operator.MULT)
        elif ctx.DIV() is not None:
            self.quadruple_list.push_operator(Operator.DIV)
        else:
            raise Exception(f"Invalid MULOP.")
        
    # Point 26
    def exitFactor(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.MULT or top_operator == Operator.DIV:
            self.generate_quadruple(top_operator)
        
    # Point 27
    def exitSumop(self, ctx):
        if ctx.PLUS() is not None:
            self.quadruple_list.push_operator(Operator.SUM)
        elif ctx.MINUS() is not None:
            self.quadruple_list.push_operator(Operator.SUB)
        else:
            raise Exception(f"Invalid SUMOP.")
        
    # Point 28
    def exitTerm(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.SUM or top_operator == Operator.SUB:
            self.generate_quadruple(top_operator)
        
    # Point 29
    def exitRelop(self, ctx):
        if ctx.EQUALS() is not None:
            self.quadruple_list.push_operator(Operator.EQ)
        elif ctx.GREATER_THAN() is not None:
            self.quadruple_list.push_operator(Operator.GT)
        elif ctx.LESS_THAN() is not None:
            self.quadruple_list.push_operator(Operator.LT)
        elif ctx.GREATER_EQUALS() is not None:
            self.quadruple_list.push_operator(Operator.GTE)
        elif ctx.LESS_EQUALS() is not None:
            self.quadruple_list.push_operator(Operator.LTE)
        elif ctx.DIFFERENT() is not None:
            self.quadruple_list.push_operator(Operator.DIFF)
        else:
            raise Exception(f"Invalid RELOP.")

    # Point 30
    def exitRel_exp(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.EQ or top_operator == Operator.GT or top_operator == Operator.LT or top_operator == Operator.GTE or top_operator == Operator.LTE or top_operator == Operator.DIFF:
            self.generate_quadruple(top_operator)

    # Point 31
    def exitAndop(self, ctx):
        if ctx.AND() is not None:
            self.quadruple_list.push_operator(Operator.AND)
        else:
            raise Exception(f"Invalid ANDOP.")
        
    # Point 32
    def exitExpress(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.AND:
            self.generate_quadruple(top_operator)

    # Point 33
    def exitOrop(self, ctx):
        if ctx.OR() is not None:
            self.quadruple_list.push_operator(Operator.OR)
        else:
            raise Exception(f"Invalid OROP.")
        
    # Point 34
    def exitExpressio(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.OR:
            self.generate_quadruple(top_operator)

    # Point 16
    def enterAssign_exp(self, ctx):
        self.quadruple_list.push_operand(self.caller_name, self.current_type)
        
    # Point 35
    def exitAssign_op(self, ctx):
        if ctx.ASSIGN() is not None:
            self.quadruple_list.push_operator(Operator.ASSIGN)
        else:
            raise Exception(f"Invalid ASSIGN.")
        
    # Point 36
    def exitAssign_exp(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.ASSIGN:
            left_operand = self.quadruple_list.pop_operand()
            result = self.quadruple_list.pop_operand()
        
            if left_operand.variable_type == Type.ID:
                raise Exception(f"Cannot assign values of structured type.")

            if left_operand.variable_type != result.variable_type:
                raise Exception(f"Type mismatch. Cannot assign value of type \'{Type(left_operand.variable_type).name}\' to variable of type \'{Type(result.variable_type).name}\'.")

            self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), left_operand.variable_name, None, result.variable_name)
    
    # Point 37
    def enterInit_assign(self, ctx):
        self.caller_name = ctx.parentCtx.ID().getText()
        self.current_type = self.dir_gen.current_type
        
    # Point 38
    def exitInit_assign(self, ctx):
       self.caller_name = ""
        
    # Point 40
    def exitTpp_return(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.RETURN:
            result = self.quadruple_list.pop_operand()
            func_obj = self.dir_gen.function_search(self.dir_gen.current_scope, self.dir_gen.current_class)
        
            if result.variable_type != func_obj.return_type:
                raise Exception(f"Type mismatch. Cannot return value of type \'{Type(result.variable_type).name}\' from function with return type \'{Type(func_obj.return_type).name}\'.")
            
            self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), None, None, result.variable_name)
        
    # Point 41
    def enterRead_var(self, ctx):
        if ctx.parentCtx.READ() is not None:
            self.quadruple_list.push_operator(Operator.READ)
        else:
            raise Exception(f"Invalid READ.")
        
    # Point 42
    def exitRead_var(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.READ:
            result = Operand(self.caller_name, self.current_type)
            if result.variable_type == Type.ID:
                raise Exception(f"Cannot read data for structured types.")
            self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), None, None, result.variable_name)
        
    # Point 43
    def enterPrint_val(self, ctx):
        if ctx.parentCtx.PRINT() is not None:
            self.quadruple_list.push_operator(Operator.PRINT)
        else:
            raise Exception(f"Invalid PRINT.")
        
    # Point 44
    def exitPrint_exp(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.PRINT:
            result = self.quadruple_list.pop_operand()
            if result.variable_type == Type.ID:
                raise Exception(f"Cannot print value of a structured type.")
            self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), None, None, result.variable_name)
        
    # Point 45
    def exitPrint_string(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.PRINT:
            result = ctx.CTE_STRING().getText()
            self.quadruple_list.push_quadruple(self.quadruple_list.pop_operator(), None, None, result)


    # Point 17
    def exitSwitch_cte(self, ctx):
        if ctx.CTE_INT() is not None:
            self.quadruple_list.push_operand(self.temp_ints.pop(0), Type.INT)
        elif ctx.CTE_CHAR() is not None:
            self.quadruple_list.push_operand(self.temp_chars.pop(0), Type.CHAR)
        else:
            raise Exception(f"Invalid constant for switch statement.")

    # Point 46
    def enterIfelse(self, ctx):
        self.quadruple_list.push_jump(Operator.FF)

    # Point 46
    def enterSwitch_stmt(self, ctx):
        self.quadruple_list.push_jump(Operator.FF)

    # Point 47
    def exitIf_expr(self, ctx):
        self.create_gotof()

    # Point 47
    def exitWhile_expr(self, ctx):
        self.create_gotof()

    # Point 48
    def enterTpp_elif(self, ctx):
        self.create_cond_goto()

    # Point 48
    def enterTpp_else(self, ctx):
        self.create_cond_goto()

    # Point 48
    def enterNext_case(self, ctx):
        self.create_cond_goto()

    # Point 48
    def enterTpp_default(self, ctx):
        self.create_cond_goto()

    # Point 49
    def exitIfelse(self, ctx):
        self.empty_jumps()

    # Point 50
    def enterSwitch_block(self, ctx):
        self.quadruple_list.push_operator(Operator.EQ)
        self.generate_quadruple(self.quadruple_list.top_operator())
        self.create_gotof()
        
    # Point 51
    def exitSwitch_stmt(self, ctx):
        self.empty_jumps()
        self.recurrent_vars.pop()
        
    # Point 52
    def enterWhile_expr(self, ctx):
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count)

    # Point 52
    def enterFor_to(self, ctx):
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count)

    # Point 53
    def exitWloop(self, ctx):
        self.create_loop_goto()

    # Point 54
    def exitFor_assign(self, ctx):
        left_operand = self.quadruple_list.pop_operand()
        result = self.quadruple_list.pop_operand()

        if left_operand.variable_type == Type.ID:
                raise Exception(f"Cannot assign values of structured type.")
    
        if left_operand.variable_type != result.variable_type:
            raise Exception(f"Type mismatch. Cannot assign value of type \'{Type(left_operand.variable_type).name}\' to variable of type \'{Type(result.variable_type).name}\'.")

        self.quadruple_list.push_quadruple(Operator.ASSIGN, left_operand.variable_name, None, result.variable_name)
        self.quadruple_list.push_operand(result.variable_name, result.variable_type)

    # Point 55
    def exitFor_to(self, ctx):
        self.quadruple_list.push_operator(Operator.LTE)
        self.generate_quadruple(self.quadruple_list.top_operator())
        self.create_gotof()
        
    # Point 56
    def exitFloop(self, ctx):
        for_var = self.recurrent_vars.pop()
        const_temp = self.get_temp(Type.INT)
        res_temp = self.get_temp(for_var.variable_type)
        self.quadruple_list.push_quadruple(Operator.SUM, for_var.variable_name, const_temp, res_temp)
        self.quadruple_list.push_quadruple(Operator.ASSIGN, res_temp, None, for_var.variable_name)
        self.create_loop_goto()
    
    # Point 57
    def exitSwitch_expr(self, ctx):
        recurrent_var = self.quadruple_list.pop_operand()
        if recurrent_var.variable_type != Type.INT and recurrent_var.variable_type != Type.CHAR:
            raise Exception(f"Cannot create switch statement with type \'{Type(recurrent_var.variable_type).name}\'.")
        
        self.recurrent_vars.push(recurrent_var)
    
    # Point 58
    def enterTpp_case(self, ctx):
        self.quadruple_list.push_operand(self.recurrent_vars.top().variable_name, self.recurrent_vars.top().variable_type)
    
    # Point 59
    def exitFor_var(self, ctx):
        self.recurrent_vars.push(Operand(self.caller_name, self.current_type))
        self.quadruple_list.push_operand(self.recurrent_vars.top().variable_name, self.recurrent_vars.top().variable_type)

    # Point 65
    def exitReturn_type(self, ctx):
        if (self.dir_gen.current_type == Type.VOID):
            self.return_state = 0
        else:
            self.return_state = 1

    # Point 39, Point 66
    def enterTpp_return(self, ctx):
        # Point 66
        if self.return_state == 0: # Return statement in void function, raises error
            raise Exception(f"Invalid return statement in void function")
        elif self.quadruple_list.top_jump() is None: # Return statement in base of function declaration
            self.return_state = 2
        
        # Point 39
        if ctx.RETURN() is not None: 
            self.quadruple_list.push_operator(Operator.RETURN)
        else:
            raise Exception(f"Invalid RETURN.")

    # Point 7, Point 61, Point 62
    def exitParam(self, ctx):
        self.dir_gen.exitParam(ctx)
        
    # Point 63
    def exitParams(self, ctx):
        self.dir_gen.set_first_quad(self.quadruple_list.quadruple_count)
        
    # Point 64, Point 67
    def exitTpp_function(self, ctx):
        # Point 67
        if self.return_state == 1: # Function needed return but no return was found outside of non-linear statements, raises error
            raise Exception(f"Missing return statement outside of non-linear statements in non-void function \'{self.dir_gen.current_scope}\'.")

        # Point 64
        self.quadruple_list.push_quadruple(Operator.ENDFUNC, None, None, None)

    # Point 7, Point 61
    def exitInit_arr(self, ctx):
        self.dir_gen.exitInit_arr(ctx)
        
    # Point 68
    def exitFunc_name(self, ctx):
        if self.is_attribute:
            func_obj = self.dir_gen.method_search(self.called_function, self.current_type_id)
        else:
            func_obj = self.dir_gen.function_search(self.called_function, self.dir_gen.current_class)
        
        size = func_obj.get_total_size()
        self.quadruple_list.push_quadruple(Operator.ERA, None, None, size)

        # Pushing tuple of Function object and its parameter count to funcalls stack
        self.p_funcalls.push([func_obj, 0])
        
    # Point 69
    def exitArgument(self, ctx):
        func_tuple = self.p_funcalls.top()
        parameter = func_tuple[0].get_param_at(func_tuple[1] - 1)
        if parameter is None:
            raise Exception(f"Too many arguments given for function \'{func_tuple[0].name}\'.")
        
        argument = self.quadruple_list.pop_operand()

        if parameter.type == argument.variable_type:
            if parameter.type == Type.ID and parameter.type_id != argument.variable_type_id:
                raise Exception(f"Expected argument of type \'{parameter.type_id}\' but received type \'{argument.variable_type_id}\'")
        else:
            raise Exception(f"Expected argument of type \'{Type(parameter.type).name}\' but received type \'{Type(argument.variable_type).name}\'")

        self.quadruple_list.push_quadruple(Operator.PARAMETER, argument.variable_name, None, parameter.name)

    # Point 70
    def enterArgument(self, ctx):
        # Increment parameter count for latest funcall
        self.p_funcalls.elements[-1][1] += 1
        
    # Point 20, Point 71, Point 72
    def exitFuncall(self, ctx):
        func_tuple = self.p_funcalls.pop()
        # Point 71
        if func_tuple[1] < len(func_tuple[0].params):
            raise Exception(f"Not enough arguments given for function \'{func_tuple[0].name}\'. Expected {len(func_tuple[0].params)} arguments but received {func_tuple[1]}.")
        
        # Point 72
        self.quadruple_list.push_quadruple(Operator.GOSUB, func_tuple[0].name, None, func_tuple[0].first_quad)

        # Point 20
        self.is_attribute = False

