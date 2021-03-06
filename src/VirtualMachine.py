import sys
import operator

from src.MachineMemory import MachineMemory, FunctionMemory, PointerMemory, InstanceMemory
from util.Enums import Operator, Type
from util.DataStructures import Stack

class VirtualMachine:
    """
    Defines the functions required to execute the intermediate code generated by the
    compiler. Recives from the compiler the General Directory, Quadruple List, and Constant Table.
    """

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
        self.global_instance_memory = []

        self.exec_stack = Stack()
        self.exec_temp = Stack()
        self.active_instances = Stack()

        global_local = self.dir_gen.dir_func["global"].address_manager.local
        global_temp = self.dir_gen.dir_func["global"].address_manager.temp
        global_pointer = self.dir_gen.dir_func["global"].address_manager.pointer
        self.exec_stack.push(FunctionMemory(global_local, global_temp, global_pointer, None, 0))
        
    def read_address(self, address):
        value = None
        if address >= 10000:
            # Compound address
            inst = address // 10000
            attr = address % 10000
            context = inst // 1000
            reduced_index = inst % 1000
            reduced_address = attr % 1000
            
            if context == 6:
                # Global instance
                value = self.global_instance_memory[reduced_index].read_address(reduced_address)
            elif context == 5:
                # Local instance
                value = self.exec_stack.top().instance_list[reduced_index].read_address(reduced_address)
            elif context == 4:
                # Pointer to instance
                pointed_address = self.exec_stack.top().pointer_memory.read_pointer(reduced_index)
                pointed_address = pointed_address * 10000 + attr
                value = self.read_address(pointed_address)
            
        else:
            # Simple address
            context = address // 1000
            reduced_address = address % 1000
            if context == 7:
                # Attribute local to a method
                value = self.active_instances.top().read_address(reduced_address)
            elif context == 4:
                # Pointer to array cell
                pointed_address = self.exec_stack.top().pointer_memory.read_pointer(reduced_address)
                value = self.read_address(pointed_address)
            elif context == 3:
                # Constant
                value = self.const_table[address]
            elif context == 2:
                # Temp
                value = self.exec_stack.top().temp_memory.read_address(reduced_address)
            elif context == 1:
                # Local
                value = self.exec_stack.top().local_memory.read_address(reduced_address)
            elif context == 0:
                # Global
                value = self.global_memory.read_address(reduced_address)
        
        if value is None:
            print("[Error] Variable not initialized.")
            sys.exit()

        return value

    def write_address(self, address, value):

        if address >= 10000:
            # Compound address
            inst = address // 10000
            attr = address % 10000
            context = inst // 1000
            reduced_index = inst % 1000
            reduced_address = attr % 1000
            
            if context == 6:
                # Global instance
                self.global_instance_memory[reduced_index].write_address(reduced_address, value)
            elif context == 5:
                # Local instance
                self.exec_stack.top().instance_list[reduced_index].write_address(reduced_address, value)
            elif context == 4:
                # Pointer to instance
                pointed_address = self.exec_stack.top().pointer_memory.read_pointer(reduced_index)
                pointed_address = pointed_address * 10000 + attr
                self.write_address(pointed_address, value)
                   
        else:
            context = address // 1000
            reduced_address = address % 1000
            if context == 7:
                # Attribute local to a method
                self.active_instances.top().write_address(reduced_address, value)
            elif context == 4:
                self.write_address(self.exec_stack.top().pointer_memory.read_pointer(reduced_address), value)
            elif context == 2:
                # Temp
                self.exec_stack.top().temp_memory.write_address(reduced_address, value)
            elif context == 1:
                # Local
                self.exec_stack.top().local_memory.write_address(reduced_address, value)
            else:
                # Global
                self.global_memory.write_address(reduced_address, value)
        
    def write_address_temp(self, address, value):
        # Write address to memory context in temporal execution stack
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
                # Perform regular division
                result = left_op / right_op
            else:
                # Perform integer division
                result = left_op // right_op
        except ZeroDivisionError:
            print("[Error] Cannot perform division by zero.")
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
            # Perform print on expression result
            print(quad.result[1:-1].replace('\\n','\n').replace('\\t', '\t'), end="")
        else:
            # Perform print on string constant
            print(self.read_address(quad.result), end="")

    def read_helper(self, address):
        value = input()
        reduced_address = address % 1000
        if reduced_address // 100 == 0:
            # INT expected
            try:
                value = int(value)
                self.write_address(address, value)
            except ValueError:
                print("[Error] Wrong input type. Expected input of type \'INT\'.")
                sys.exit()
        elif reduced_address // 100 == 1:
            # FLOAT expected
            try:
                value = float(value)
                self.write_address(address, value)
            except ValueError:
                print("[Error] Wrong input type. Expected input of type \'FLOAT\'")
                sys.exit()
        else: 
            # CHAR expected
            if len(value) == 1:
                self.write_address(address, value)
            else:
                print("[Error] Wrong input type. Expected input of type \'CHAR\'.")
                sys.exit()
    
    def do_read(self, quad):
        context = quad.result // 1000
        reduced_address = quad.result % 1000
        if context == 4:
            # Get the address inside the pointer, then perform read for obtained address
            pointed_address = self.exec_stack.top().pointer_memory.read_pointer(reduced_address)
            self.read_helper(pointed_address)
        else:
            # Perform read for recieved address
            self.read_helper(quad.result)

    def do_goto(self, quad):
        # Set next quadruple to the index inside the quadruple's result
        self.exec_stack.elements[-1].next_quad = quad.result - 1

    def do_gotof(self, quad):
        # Change next quadruple to the index in result depending on condition being false
        operand = True if self.read_address(quad.left_operand) != 0 else False
        if not operand:
            self.exec_stack.elements[-1].next_quad = quad.result - 1
            
    def do_era(self, quad):
        is_method = False
        if quad.left_operand is None:
            # Function is global
            func_obj = self.dir_gen.dir_func[quad.result]
        else:
            # Function is method of a class
            func_obj = self.dir_gen.dir_class[quad.left_operand].methods[quad.result]
            is_method = True

        # Save all address managers needed to create local context
        func_local = func_obj.address_manager.local
        func_temp = func_obj.address_manager.temp
        func_pointer = func_obj.address_manager.pointer

        # Create new context and push it to temporal execution stack
        new_context = FunctionMemory(func_local, func_temp, func_pointer, func_obj.return_addr, func_obj.first_quad - 1, is_method)
        self.exec_temp.push(new_context)

    def do_parameter(self, quad):
        argument = self.read_address(quad.left_operand)
        self.write_address_temp(quad.result, argument)

    def do_gosub(self, quad):
        new_context = self.exec_temp.pop()
        self.exec_stack.push(new_context)

    def do_endfunc(self):
        if self.exec_stack.top().is_method:
            self.active_instances.pop()
        self.exec_stack.pop()

    def do_return(self, quad):
        value = self.read_address(quad.result)
        self.write_address(self.exec_stack.top().return_addr, value)
        self.do_endfunc()

    def do_gomain(self, quad):
        # Push local context for main to execution stack
        self.exec_stack.pop()
        main_local = self.dir_gen.dir_func["main"].address_manager.local
        main_temp = self.dir_gen.dir_func["main"].address_manager.temp
        main_pointer = self.dir_gen.dir_func["main"].address_manager.pointer
        self.exec_stack.push(FunctionMemory(main_local, main_temp, main_pointer, None, quad.result - 1))
    
    def do_verify(self, quad):
        # Get value for index
        s = self.read_address(quad.left_operand)

        # Get value for dimension size
        d = 0 if quad.right_operand == None else quad.right_operand

        if s < 0 or s >= d:
            print("[Error] Index out of bounds.")
            sys.exit()
    
    def do_point(self, quad):
        # Calculate the necessary variables to write pointer
        base = quad.left_operand
        offset = self.read_address(quad.right_operand)
        address = quad.result % 1000
        
        # Write the calculated address to the pointer in quadruple's result
        self.exec_stack.top().pointer_memory.write_pointer(address, base + offset)
    
    def do_inst(self, quad):
        # Get address manager for the instance's class
        attr_dir = self.dir_gen.dir_class[quad.result].address_manager

        # Iterate in case of declaration of instance array
        for _ in range(quad.left_operand):
            if quad.right_operand:
                # Append memory needed for global instance
                self.global_instance_memory.append(InstanceMemory(attr_dir))
            else:
                # Append memory needed for local instance
                self.exec_stack.elements[-1].instance_list.append(InstanceMemory(attr_dir))

    def do_method(self, address):
        if address == -1:
            self.active_instances.push(self.active_instances.top())
        else:
            context = address // 1000
            reduced_address = address % 1000
            
            if context == 6:
                # Method of a global instance
                self.active_instances.push(self.global_instance_memory[reduced_address])
            elif context == 5:
                # Method of a local instance
                self.active_instances.push(self.exec_stack.top().instance_list[reduced_address])
            elif context == 4:
                # Method of a pointer
                pointed_address = self.exec_stack.top().pointer_memory.read_pointer(reduced_address)
                self.do_method(pointed_address)

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
            elif quad.operator == Operator.VERIFY:
                self.do_verify(quad)
            elif quad.operator == Operator.POINT:
                self.do_point(quad)
            elif quad.operator == Operator.INST:
                self.do_inst(quad)
            elif quad.operator == Operator.METHOD:
                self.do_method(quad.result)
            else:
                print(f"Unexpected operator {Operator(quad.operator)}.")
                sys.exit()
            
            self.exec_stack.elements[-1].advance()