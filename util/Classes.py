from src.VirtualMemory import FunctionAddressManager
from util.Enums import Type, Level, Operator

class UserClass:
    def __init__(self, name, parent = None):
        self.name = name
        self.methods = dict()
        self.attributes = dict()
        self.parent = parent

    def __repr__(self):
        return f'\nClass\n \tName: {self.name}\n \tParent: {self.parent}\n \tAttributes: {self.attributes}\n \tMethods{self.methods}'

    def set_data_from_parent(self, parent):
        for (var_name, var_obj) in parent.attributes.items():
            self.attributes[var_name] = var_obj
        
        for (method_name, method_obj) in parent.methods.items():
            self.methods[method_name] = method_obj

    def set_parent(self, parent):
        self.parent = parent.name
        self.set_data_from_parent(parent)

class Function:
    def __init__(self, name, return_type = Type.VOID, return_addr = None, level = None, original_class = None):
        self.name = name
        self.level = level
        self.return_type = return_type
        self.return_addr = return_addr
        self.original_class = original_class
        self.variables = dict()
        self.params = []
        self.first_quad = None
        self.address_manager = FunctionAddressManager()

    def __repr__(self):
        return f'\n\tFunction\n \tName: {self.name}\n \tLevel: {self.level}\n \tReturn Type: {Type(self.return_type).name}\n \tReturn Address: {self.return_addr}\n \tOriginal Class: {self.original_class}\n \tVariables{self.variables}\n \tParams: {self.params}\n \tFirst Quad: {self.first_quad}\n \t{self.address_manager}'
    
    def set_level(self, level):
        self.level = level

    def set_original_class(self, original_class):
        self.original_class = original_class

    def get_local_address(self, type, d1 = None, d2 = None):
        return self.address_manager.get_local_address(type, d1, d2)
    
    def get_temp_address(self, type):
        return self.address_manager.get_temp_address(type)

    def return_temp_address(self, address):
        self.address_manager.return_temp_address(address)

    def add_param(self, variable_address, variable_type, variable_type_id):
        self.params.append(Parameter(variable_address, variable_type, variable_type_id))
        
    def set_first_quad(self, first_quad):
        self.first_quad = first_quad
    
    def get_total_size(self):
        return self.address_manager.get_size()

    def get_param_at(self, k):
        if k >= len(self.params):
            return None
        return self.params[k]

class Variable:
    def __init__(self, name, type, type_id = None, address = None, level = None, original_class = None, d1=None, d2=None):
        self.name = name
        self.type = type
        if self.type == Type.ID:
            self.type_id = type_id
        else:
            self.type_id = None

        self.address = address
        self.level = level
        self.original_class = original_class
        
        self.d1 = d1
        self.d2 = d2
        self.dim_count = 0
        if d2 is not None:
            self.dim_count = 2
        elif d1 is not None:
            self.dim_count = 1
        
        
    def __repr__(self):
        return f'\n\t\tAddress: {self.address} Variable Name: {self.name} Level: {self.level} Type: {Type(self.type).name} Type ID: {self.type_id} Original Class: {self.original_class} D1: {self.d1} D2: {self.d2}'

    def set_level(self, level):
        self.level = level

    def set_original_class(self, original_class):
        self.original_class = original_class

class Parameter:
    def __init__(self, address, type, type_id = None):
        self.address = address
        self.type = type
        if self.type == Type.ID:
            self.type_id = type_id
        else:
            self.type_id = None

    def __repr__(self):
        return f"Address: {self.address}, Type: {self.type}, Type ID: {self.type_id}"

class Operand:
    def __init__(self, address, variable_type, variable_type_id = None):
        self.address = address
        self.variable_type = variable_type
        if self.variable_type == Type.ID:
            self.variable_type_id = variable_type_id
        else:
            self.variable_type_id = None

    def __repr__(self):
        return f'\nOperand \tAddress: {self.address} \tType: {Type(self.variable_type).name}\n'

class Quadruple:
    def __init__(self, operator, left_operand, right_operand, result, index):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
        self.index = index
    
    def __repr__(self):
        return f'\n {self.index} Operator: {Operator(self.operator).name}\t Left Operand: {self.left_operand}\t Right Operand: {self.right_operand}\t Result: {self.result}'
