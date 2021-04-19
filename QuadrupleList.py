from util.DataStructures import Stack, Queue

class Quadruple:
    def __init__(self, operator, left_operand, right_operand, result):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
    
    def __repr__(self):
        return f'\Operator: {self.operator}\n \tLeft Operand: {self.left_operand}\n \tRight Operand: {self.right_operand}\n \tResult: {self.result}'

class QuadrupleList:
    quadruple_list = Queue()
    p_oper = Stack()
    p_vars = Stack()
    p_types = Stack()

    def __repr__(self):
        return f'{self.quadruple_list}'

    def push_operator(self, operator):
        self.p_oper.push(operator)

    def push_variable(self, variable):
        self.p_vars.push(variable)
    
    def push_type(self, type_enum):
        self.p_types.push(type_enum)
    
    def push_quadruple(self, quadruple):
        self.quadruple_list.push(quadruple)
    
    def pop_operator(self):
        return self.p_oper.pop()

    def pop_variable(self):
        return self.p_vars.pop()
    
    def pop_type(self):
        return self.p_types.pop()
    
    def pop_quadruple(self):
        return self.quadruple_list.pop()

    def top_operator(self):
        return self.p_oper.top()
