from util.DataStructures import Stack, Queue
from util.Classes import Quadruple, Operand
from util.Enums import Type, Operator

class QuadrupleList:
    quadruple_list = Queue()
    p_operators = Stack()
    p_operands = Stack()
    p_jumps = Stack()
    quadruple_count = 0

    def __repr__(self):
        return f'{self.quadruple_list}'

    def push_operator(self, operator):
        self.p_operators.push(operator)

    def push_operand(self, variable_name, var_type, var_type_id = None):
        self.p_operands.push(Operand(variable_name, var_type, var_type_id))

    def push_quadruple(self, operator, left_operand, right_operand, result):
        self.quadruple_list.push(Quadruple(operator, left_operand, right_operand, result, self.quadruple_count))
        self.quadruple_count += 1
        
    def push_jump(self, jump):
        self.p_jumps.push(jump)
    
    def update_quadruple(self, index, result):
        quad = self.quadruple_list.at(index)
        quad.result = result
        self.quadruple_list.replace(index, quad)
    
    def pop_operator(self):
        return self.p_operators.pop()

    def pop_operand(self):
        return self.p_operands.pop()
    
    def pop_quadruple(self):
        return self.quadruple_list.pop()
    
    def pop_jump(self):
        return self.p_jumps.pop()

    def top_operator(self):
        if self.p_operators.empty():
            return None
        return self.p_operators.top()
    
    def top_jump(self):
        if self.p_jumps.empty():
            return None
        return self.p_jumps.top()
