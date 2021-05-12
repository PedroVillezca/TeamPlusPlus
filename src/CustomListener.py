import sys

from antlr4 import *
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

from src.DirGen import DirGen
from src.QuadrupleList import QuadrupleList
from util.Classes import Operand
from util.DataStructures import Stack
from util.Enums import Operator, Type, Level
from util.SemanticCube import semantic_cube

class CustomListener(TeamPlusPlusListener):
    dir_gen = DirGen()
    quadruple_list = QuadrupleList()

    current_type = None
    current_type_id = None
    is_attribute = False
    caller_name = ""
    caller_address = None
    recurrent_vars = Stack()

    return_state = 0
    called_function = ""
    called_function_addr = None
    p_funcalls = Stack()


    def __repr__(self):
        return f'\nDir Gen: \n {self.dir_gen} \n\n Quadruple List: \n {self.quadruple_list}'

    def get_temp(self, result_type):
        # Add temp var to current function depending on type
        return self.dir_gen.get_temp_address(result_type)

    def recycle_temp_address(self, address):
        if address // 1000 == 2:
            # Address belongs to a temporary variable
            if self.recurrent_vars.empty() or address != self.recurrent_vars.top().address:
                # Address is not being used as a recurrent variable, recycle
                self.dir_gen.return_temp_address(address)

    def push_quadruple(self, operator, left_operand, right_operand, result):
        self.quadruple_list.push_quadruple(operator, left_operand, right_operand, result)
        
        if left_operand is not None:
            self.recycle_temp_address(left_operand)
        if right_operand is not None:
            self.recycle_temp_address(right_operand)

    def generate_quadruple(self, top_operator):
        right_operand = self.quadruple_list.pop_operand()
        left_operand = self.quadruple_list.pop_operand()
        result_type = semantic_cube[left_operand.variable_type][right_operand.variable_type][top_operator]

        if result_type is None:
            print(f"[Error] Invalid operand types \'{Type(left_operand.variable_type).name}\' and \'{Type(right_operand.variable_type).name}\' for operator {Operator(self.quadruple_list.top_operator()).name}.")
            sys.exit()

        result_address = self.get_temp(result_type)
        
        self.push_quadruple(self.quadruple_list.pop_operator(), left_operand.address, right_operand.address, result_address)
        self.quadruple_list.push_operand(result_address, result_type)
        
    
    def create_gotof(self):
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count)
        left_operand = self.quadruple_list.pop_operand()
        if left_operand.variable_type != Type.INT:
            print(f"[Error] Cannot evaluate value of type {Type(left_operand.variable_type).name} for conditions.")
            sys.exit()

        self.push_quadruple(Operator.GOTOF, left_operand.address, None, None)
    
    def create_cond_goto(self):
        self.push_quadruple(Operator.GOTO, None, None, None)
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count - 1)

    def create_loop_goto(self):
        self.push_quadruple(Operator.GOTO, None, None, None)
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(self.quadruple_list.quadruple_count-1, index)
        
    
    def empty_jumps(self):
        while self.quadruple_list.top_jump() != Operator.FF:
            index = self.quadruple_list.pop_jump()
            self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        self.quadruple_list.pop_jump()

    # Point 1, Point 73
    def enterProgram(self, ctx):
        # Point 1
        self.dir_gen.enterProgram(ctx)

        # Point 73
        self.push_quadruple(Operator.GOTO, None, None, None)
        self.quadruple_list.push_jump(self.quadruple_list.quadruple_count - 1)

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
    
    # Point 10, Point 74
    def enterMain(self, ctx):
        # Point 10
        self.dir_gen.enterMain(ctx)

        # Point 74
        index = self.quadruple_list.pop_jump()
        self.quadruple_list.update_quadruple(index, self.quadruple_list.quadruple_count)
        
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
            print(f"[Error] Variable \'{var_name}\' does not exist.")
            sys.exit()

        if var_obj.level == Level.PRIVATE and var_obj.original_class != self.dir_gen.current_class:
            print(f"[Error] Attribute \'{var_name}\' is private to class {var_obj.original_class}.")
            sys.exit()

        self.current_type = var_obj.type
        if var_obj.type == Type.ID:
            self.current_type_id = var_obj.type_id
        self.caller_name = var_name
        self.caller_address = var_obj.address

    # Point 20
    def exitVar(self, ctx):
        self.is_attribute = False

    # Point 60
    def enterAttr(self, ctx):
        var_name = ctx.ID().getText()
        var_obj = self.dir_gen.attribute_search(var_name, self.current_type_id)

        if var_obj is None:
            print(f"[Error] Variable \'{var_name}\' does not exist.")
            sys.exit()
        
        if var_obj.level == Level.PRIVATE and var_obj.original_class != self.dir_gen.current_class:
            print(f"[Error] Attribute \'{var_name}\' is private to class {var_obj.original_class}.")
            sys.exit()

        self.current_type = var_obj.type
        if var_obj.type == Type.ID:
            self.current_type_id = var_obj.type_id
        self.caller_name += var_name
        self.caller_address = var_obj.address
        
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
        self.quadruple_list.push_operand(self.caller_address, self.current_type, self.current_type_id)

    # Point 17
    def exitVal_cte(self, ctx):
        if ctx.CTE_INT() is not None:
            self.quadruple_list.push_operand(self.get_temp(Type.INT), Type.INT)
        elif ctx.CTE_FLOAT() is not None:
            self.quadruple_list.push_operand(self.get_temp(Type.FLOAT), Type.FLOAT)
        elif ctx.CTE_CHAR() is not None:
            self.quadruple_list.push_operand(self.get_temp(Type.CHAR), Type.CHAR)
        
    # Point 18
    def enterFunc_name(self, ctx):
        func_name = ctx.ID().getText()

        if self.is_attribute:
            func_obj = self.dir_gen.method_search(func_name, self.current_type_id)
        else:
            func_obj = self.dir_gen.function_search(func_name, self.dir_gen.current_class)

        if func_obj is None:
            print(f"[Error] Function \'{func_name}\' does not exist.")
            sys.exit()

        if func_obj.level == Level.PRIVATE and func_obj.original_class != self.dir_gen.current_class:
            print(f"[Error] Function \'{func_name}\' is private to class {func_obj.original_class}.")
            sys.exit()
        
        self.current_type = func_obj.return_type
        self.called_function = func_name
        
    # Point 19
    def exitVal_funcall(self, ctx):
        temp_address = self.get_temp(self.current_type)
        
        if temp_address is None:
            print("[Error] Functions must return primitive types when used in expressions.")
            sys.exit()
        
        self.push_quadruple(Operator.ASSIGN, self.called_function_addr, None, temp_address)
        self.quadruple_list.push_operand(temp_address, self.current_type)
        
    # Point 21
    def exitUnop(self, ctx):
        if ctx.PLUS() is not None:
            self.quadruple_list.push_operator(Operator.POS)
        elif ctx.MINUS() is not None:
            self.quadruple_list.push_operator(Operator.NEG)
        elif ctx.NOT() is not None:
            self.quadruple_list.push_operator(Operator.NOT)
        
    # Point 22
    def exitFactor_elem(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.POS or top_operator == Operator.NEG or top_operator == Operator.NOT:
            left_operand = self.quadruple_list.pop_operand()
        
            if left_operand.variable_type != Type.INT and left_operand.variable_type != Type.FLOAT:
                print(f"Invalid operand type \'{Type(left_operand.variable_type).name}\' for operator {Operator(self.quadruple_list.top_operator()).name}.")
                sys.exit()
            
            if left_operand.variable_type == Type.INT or top_operator == Operator.NOT:
                result_address = self.get_temp(Type.INT)
                result_type = Type.INT
            else:
                result_address = self.get_temp(Type.FLOAT)
                result_type = Type.FLOAT

            self.push_quadruple(self.quadruple_list.pop_operator(), left_operand.address, None, result_address)
            self.quadruple_list.push_operand(result_address, result_type)
        
    # Point 23
    def enterFake_bottom(self, ctx):
        self.quadruple_list.push_operator(Operator.FF)
        
    # Point 24
    def exitFake_bottom(self, ctx):
        self.quadruple_list.pop_operator()
        
    # Point 25
    def exitMulop(self, ctx):
        if ctx.MULT() is not None:
            self.quadruple_list.push_operator(Operator.MULT)
        elif ctx.DIV() is not None:
            self.quadruple_list.push_operator(Operator.DIV)
        
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

    # Point 30
    def exitRel_exp(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.EQ or top_operator == Operator.GT or top_operator == Operator.LT or top_operator == Operator.GTE or top_operator == Operator.LTE or top_operator == Operator.DIFF:
            self.generate_quadruple(top_operator)

    # Point 31
    def exitAndop(self, ctx):
        self.quadruple_list.push_operator(Operator.AND)
        
    # Point 32
    def exitExpress(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.AND:
            self.generate_quadruple(top_operator)

    # Point 33
    def exitOrop(self, ctx):
        self.quadruple_list.push_operator(Operator.OR)
        
    # Point 34
    def exitExpressio(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.OR:
            self.generate_quadruple(top_operator)

    # Point 16
    def enterAssign_exp(self, ctx):
        self.quadruple_list.push_operand(self.caller_address, self.current_type)
        
    # Point 35
    def exitAssign_op(self, ctx):
        self.quadruple_list.push_operator(Operator.ASSIGN)
        
    # Point 36
    def exitAssign_exp(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.ASSIGN:
            left_operand = self.quadruple_list.pop_operand()
            result = self.quadruple_list.pop_operand()
        
            if left_operand.variable_type == Type.ID:
                print("[Error] Cannot assign values of structured type.")
                sys.exit()

            if left_operand.variable_type != result.variable_type:
                print(f"[Error] Type mismatch. Cannot assign value of type \'{Type(left_operand.variable_type).name}\' to variable of type \'{Type(result.variable_type).name}\'.")
                sys.exit()
            self.push_quadruple(self.quadruple_list.pop_operator(), left_operand.address, None, result.address)
    
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
                print(f"[Error] Type mismatch. Cannot return value of type \'{Type(result.variable_type).name}\' from function with return type \'{Type(func_obj.return_type).name}\'.")
                sys.exit()

            self.push_quadruple(self.quadruple_list.pop_operator(), None, None, result.address)
        
    # Point 41
    def enterRead_var(self, ctx):
        self.quadruple_list.push_operator(Operator.READ)
        
    # Point 42
    def exitRead_var(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.READ:
            result = Operand(self.caller_address, self.current_type)

            if result.variable_type == Type.ID:
                print("[Error] Cannot read data for structured types.")
                sys.exit()
                
            self.push_quadruple(self.quadruple_list.pop_operator(), None, None, result.address)
        
    # Point 43
    def enterPrint_val(self, ctx):
        self.quadruple_list.push_operator(Operator.PRINT)
        
    # Point 44
    def exitPrint_exp(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.PRINT:
            result = self.quadruple_list.pop_operand()

            if result.variable_type == Type.ID:
                print("[Error] Cannot print value of a structured type.")
                sys.exit()
                
            self.push_quadruple(self.quadruple_list.pop_operator(), None, None, result.address)
        
    # Point 45
    def exitPrint_string(self, ctx):
        top_operator = self.quadruple_list.top_operator()
        if top_operator == Operator.PRINT:
            result = ctx.CTE_STRING().getText()
            self.push_quadruple(self.quadruple_list.pop_operator(), None, None, result)


    # Point 17
    def exitSwitch_cte(self, ctx):
        if ctx.CTE_INT() is not None:
            self.quadruple_list.push_operand(self.get_temp(Type.INT), Type.INT)
        elif ctx.CTE_CHAR() is not None:
            self.quadruple_list.push_operand(self.get_temp(Type.CHAR), Type.CHAR)

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
            print("[Error] Cannot assign values of structured type.")
            sys.exit()
        if left_operand.variable_type != result.variable_type:
            print(f"[Error] Type mismatch. Cannot assign value of type \'{Type(left_operand.variable_type).name}\' to variable of type \'{Type(result.variable_type).name}\'.")
            sys.exit()

        self.push_quadruple(Operator.ASSIGN, left_operand.address, None, result.address)
        self.quadruple_list.push_operand(result.address, result.variable_type)

    # Point 55
    def exitFor_to(self, ctx):
        self.quadruple_list.push_operator(Operator.LTE)
        self.generate_quadruple(self.quadruple_list.top_operator())
        self.create_gotof()
        
    # Point 56
    def exitFloop(self, ctx):
        for_var = self.recurrent_vars.pop()
        const_temp_address = self.get_temp(Type.INT)
        res_temp_address = self.get_temp(for_var.variable_type)
        self.push_quadruple(Operator.SUM, for_var.address, const_temp_address, res_temp_address)
        self.push_quadruple(Operator.ASSIGN, res_temp_address, None, for_var.address)
        self.create_loop_goto()
    
    # Point 57
    def exitSwitch_expr(self, ctx):
        recurrent_var = self.quadruple_list.pop_operand()
        if recurrent_var.variable_type != Type.INT and recurrent_var.variable_type != Type.CHAR:
            print(f"[Error] Cannot create switch statement with type \'{Type(recurrent_var.variable_type).name}\'.")
            sys.exit()

        self.recurrent_vars.push(recurrent_var)
    
    # Point 58
    def enterTpp_case(self, ctx):
        self.quadruple_list.push_operand(self.recurrent_vars.top().address, self.recurrent_vars.top().variable_type)
    
    # Point 59
    def exitFor_var(self, ctx):
        self.recurrent_vars.push(Operand(self.caller_address, self.current_type))
        self.quadruple_list.push_operand(self.recurrent_vars.top().address, self.recurrent_vars.top().variable_type)

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
            print("[Error] Invalid return statement in void function")
            sys.exit()
        elif self.quadruple_list.p_jumps.size() == 1: # Return statement in base of function declaration
            self.return_state = 2
        
        # Point 39
        self.quadruple_list.push_operator(Operator.RETURN)

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
            print(f"[Error] Missing return statement outside of non-linear statements in non-void function \'{self.dir_gen.current_scope}\'.")
            sys.exit()

        # Point 64
        self.push_quadruple(Operator.ENDFUNC, None, None, None)

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
        self.push_quadruple(Operator.ERA, None, None, size)

        # Pushing tuple of Function object and its parameter count to funcalls stack
        self.p_funcalls.push([func_obj, 0])
        
    # Point 69
    def exitArgument(self, ctx):
        func_tuple = self.p_funcalls.top()
        parameter = func_tuple[0].get_param_at(func_tuple[1] - 1)
        if parameter is None:
            print(f"[Error] Too many arguments given for function \'{func_tuple[0].name}\'.")
            sys.exit()
            
        argument = self.quadruple_list.pop_operand()

        if parameter.type == argument.variable_type:
            if parameter.type == Type.ID and parameter.type_id != argument.variable_type_id:
                print(f"[Error] Expected argument of type \'{parameter.type_id}\' but received type \'{argument.variable_type_id}\'")
                sys.exit()
        else:
            print(f"[Error] Expected argument of type \'{Type(parameter.type).name}\' but received type \'{Type(argument.variable_type).name}\'")
            sys.exit()

        self.push_quadruple(Operator.PARAMETER, argument.address, None, parameter.address)

    # Point 70
    def enterArgument(self, ctx):
        # Increment parameter count for latest funcall
        self.p_funcalls.elements[-1][1] += 1
        
    # Point 20, Point 71, Point 72
    def exitFuncall(self, ctx):
        func_tuple = self.p_funcalls.pop()
        self.current_type = func_tuple[0].return_type
        self.called_function_addr = func_tuple[0].return_addr
        # Point 71
        if func_tuple[1] < len(func_tuple[0].params):
            print(f"[Error] Not enough arguments given for function \'{func_tuple[0].name}\'. Expected {len(func_tuple[0].params)} arguments but received {func_tuple[1]}.")
            sys.exit()

        # Point 72
        self.quadruple_list.push_quadruple(Operator.GOSUB, func_tuple[0].name, None, func_tuple[0].first_quad)

        # Point 20
        self.is_attribute = False
