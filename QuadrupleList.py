from util.DataStructures import Stack, Queue

class Operand:
    def __init__(self, variable_name, variable_type):
        self.variable_name = variable_name
        self.variable_type = variable_type

    def __repr__(self):
        return f'\nOperand \tName: {self.variable_name} \tType: {self.variable_type}\n'

class Quadruple:
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
    
    def __repr__(self):
        return f'\nOperator: {self.operator}\n Left Operand: {self.left_operand}\n Right Operand: {self.right_operand}\n Result: {self.result}\n'

class QuadrupleList:
    quadruple_list = Queue()
    p_operators = Stack()
    p_operands = Stack()

    def __repr__(self):
        return f'{self.quadruple_list}'

    def push_operator(self, operator):
        self.p_operators.push(operator)

    def push_operand(self, variable_name, var_type):
        self.p_operands.push(Operand(variable_name, var_type))

    def push_quadruple(self, operator, left_operand, right_operand, result):
        self.quadruple_list.push(Quadruple(operator, left_operand, right_operand, result))
    
    def pop_operator(self):
        return self.p_operators.pop()

    def pop_operand(self):
        return self.p_operands.pop()
    
    def pop_quadruple(self):
        return self.quadruple_list.pop()

    def top_operator(self):
        if self.p_operators.empty():
            return None
        return self.p_operators.top()
