import sys
import operator

from src.MachineMemory import MachineMemory, FunctionMemory
# from src.DirGen import DirGen
from util.Enums import Operator, Type
from util.DataStructures import Stack

class VirtualMachine:
    def __init__(self, dir_gen, quad_list):
        self.dir_gen = dir_gen
        self.quad_list = quad_list

        # Invert constant table indexes to enable searching by address instead of value
        self.const_table = {
            **{y:x for x, y in dir_gen.const_address_manager.const_table[Type.INT].items()},
            **{y:x for x, y in dir_gen.const_address_manager.const_table[Type.FLOAT].items()},
            **{y:x for x, y in dir_gen.const_address_manager.const_table[Type.CHAR].items()}
        }
        
        self.global_memory = MachineMemory(dir_gen.global_address_manager)

        self.exec_stack = Stack()
        self.exec_temp = Stack()
        global_local = self.dir_gen.dir_func["global"].address_manager.local
        global_temp = self.dir_gen.dir_func["global"].address_manager.temp
        self.exec_stack.push(FunctionMemory(global_local, global_temp, None, 0))
        
    def read_address(self, address):
        context = address // 1000
        reduced_address = address % 1000
        if context == 3:
            # Constant
            value = self.const_table[address]
        elif context == 2:
            # Temp
            value = self.exec_stack.top().temp_memory.read_address(reduced_address)
        elif context == 1:
            # Local
            value = self.exec_stack.top().local_memory.read_address(reduced_address)
        else:
            # Global
            value = self.global_memory.read_address(reduced_address)
        
        if value is None:
            print("[Error] Variable not initialized.")
            sys.exit()

    def write_address(self, address, value):
        context = address // 1000
        reduced_address = address % 1000
        if context == 2: # Temp
            self.exec_stack.top().temp_memory.write_address(reduced_address, value)
        elif context == 1: # Local
            self.exec_stack.top().local_memory.write_address(reduced_address, value)
        else: # Global
            self.global_memory.write_address(reduced_address, value)
        
    def write_address_temp(self, address, value):
        reduced_address = address % 1000
        self.exec_temp.top().local_memory.write_address(reduced_address, value)

    def do_relop(self, quad, op):
        left_op = self.read_address(quad.left_operand)
        right_op = self.read_address(quad.right_operand)
        result = op(left_op, right_op)
        self.write_address(quad.result, int(result))

    def do_arithmetic(self, quad, op):
        left_op = self.read_address(quad.left_operand)
        right_op = self.read_address(quad.right_operand)
        result = op(left_op, right_op)
        self.write_address(quad.result, result)

    def do_div(self, quad):
        left_op = self.read_address(quad.left_operand)
        right_op = self.read_address(quad.right_operand)

        left_type = (quad.left_operand // 100) % 10
        right_type = (quad.right_operand // 100) % 10

        try:
            if left_type != Type.INT or right_type != Type.INT:
                result = left_op / right_op
            else:
                result = left_op // right_op
        except ZeroDivisionError:
            print("[Error] Can't perform division by zero.")
            sys.exit()

        self.write_address(quad.result, result)
    
    def do_unary(self, quad, op):
        operand = self.read_address(quad.left_operand)
        result = op(operand)
        self.write_address(quad.result, result)

    def do_and(self, quad):
        left_op = True if self.read_address(quad.left_operand) != 0 else False
        right_op = True if self.read_address(quad.right_operand) != 0 else False
        result = int(left_op and right_op)
        self.write_address(quad.result, result)
    
    def do_or(self, quad):
        left_op = True if self.read_address(quad.left_operand) != 0 else False
        right_op = True if self.read_address(quad.right_operand) != 0 else False
        result = int(left_op or right_op)
        self.write_address(quad.result, result)
    
    def do_not(self, quad):
        operand = self.read_address(quad.left_operand)
        result = not operand
        self.write_address(quad.result, int(result))
    
    def do_assign(self, quad):
        value = self.read_address(quad.left_operand)
        self.write_address(quad.result, value)

    def do_print(self, quad):
        if isinstance(quad.result, str):
            print(quad.result[1:-1])
        else:
            print(self.read_address(quad.result))
    
    def do_read(self, quad):
        value = input()
        reduced_address = quad.result % 1000
        if reduced_address // 100 == 0:
            # INT expected
            try:
                value = int(value)
                self.write_address(quad.result, value)
            except ValueError:
                print("[Error] Wrong input type. Expected input of type \'INT\'.")
                sys.exit()
        elif reduced_address // 100 == 1:
            # FLOAT expected
            try:
                value = float(value)
                self.write_address(quad.result, value)
            except ValueError:
                print("[Error] Wrong input type. Expected input of type \'FLOAT\'")
                sys.exit()
        else: 
            # CHAR expected
            if len(value) == 1:
                self.write_address(quad.result, value)
            else:
                print("[Error] Wrong input type. Expected input of type \'CHAR\'.")
                sys.exit()

    def do_goto(self, quad):
        self.exec_stack.elements[-1].next_quad = quad.result - 1

    def do_gotof(self, quad):
        operand = True if self.read_address(quad.left_operand) != 0 else False
        if not operand:
            self.exec_stack.elements[-1].next_quad = quad.result - 1
            
    def do_era(self, quad):
        if quad.left_operand is None:
            # Function is global
            func_obj = self.dir_gen.dir_func[quad.result]
        else:
            # Function is method of a class
            func_obj = self.dir_gen.dir_class[quad.left_operand].methods[quad.result]

        func_local = func_obj.address_manager.local
        func_temp = func_obj.address_manager.temp

        new_context = FunctionMemory(func_local, func_temp, func_obj.return_addr, func_obj.first_quad - 1)
        self.exec_temp.push(new_context)

    def do_parameter(self, quad):
        argument = self.read_address(quad.left_operand)
        self.write_address_temp(quad.result, argument)

    def do_gosub(self, quad):
        new_context = self.exec_temp.pop()
        self.exec_stack.push(new_context)

    def do_endfunc(self):
        self.exec_stack.pop()

    def do_return(self, quad):
        value = self.read_address(quad.result)
        self.write_address(self.exec_stack.top().return_addr, value)
        self.do_endfunc()

    def do_gomain(self, quad):
        self.exec_stack.pop()
        main_local = self.dir_gen.dir_func["main"].address_manager.local
        main_temp = self.dir_gen.dir_func["main"].address_manager.temp
        self.exec_stack.push(FunctionMemory(main_local, main_temp, None, quad.result - 1))

    def run(self):
        while self.exec_stack.top().next_quad < self.quad_list.size():
            quad = self.quad_list.elements[self.exec_stack.top().next_quad]

            if quad.operator == Operator.OR:
                self.do_or(quad)
            elif quad.operator == Operator.AND:
                self.do_and(quad)
            elif quad.operator == Operator.EQ:
                self.do_relop(quad, operator.eq)
            elif quad.operator == Operator.GT:
                self.do_relop(quad, operator.gt)
            elif quad.operator == Operator.LT:
               self.do_relop(quad, operator.lt)
            elif quad.operator == Operator.GTE:
                self.do_relop(quad, operator.ge)
            elif quad.operator == Operator.LTE:
                self.do_relop(quad, operator.le)
            elif quad.operator == Operator.DIFF:
                self.do_relop(quad, operator.ne)
            elif quad.operator == Operator.MULT:
                self.do_arithmetic(quad, operator.mul)
            elif quad.operator == Operator.DIV:
                self.do_div(quad)
            elif quad.operator == Operator.SUM:
                self.do_arithmetic(quad, operator.add)
            elif quad.operator == Operator.SUB:
                self.do_arithmetic(quad, operator.sub)
            elif quad.operator == Operator.POS:
                self.do_unary(quad, operator.pos)
            elif quad.operator == Operator.NEG:
                self.do_unary(quad, operator.neg)
            elif quad.operator == Operator.NOT:
                self.do_not(quad)
            elif quad.operator == Operator.ASSIGN:
                self.do_assign(quad)
            elif quad.operator == Operator.RETURN:
                self.do_return(quad)
            elif quad.operator == Operator.READ:
                self.do_read(quad)
            elif quad.operator == Operator.PRINT:
                self.do_print(quad)
            elif quad.operator == Operator.GOTO:
                self.do_goto(quad)
            elif quad.operator == Operator.GOTOF:
                self.do_gotof(quad)
            elif quad.operator == Operator.GOSUB:
                self.do_gosub(quad)
            elif quad.operator == Operator.PARAMETER:
                self.do_parameter(quad)
            elif quad.operator == Operator.ERA:
                self.do_era(quad)
            elif quad.operator == Operator.ENDFUNC:
                self.do_endfunc()
            elif quad.operator == Operator.GOMAIN:
                self.do_gomain(quad)
            else:
                print(f"Unexpected operator {Operator(quad.operator)}.")
                sys.exit()
            
            self.exec_stack.elements[-1].advance()