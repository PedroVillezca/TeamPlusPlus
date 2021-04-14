from antlr4 import *
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

from enum import Enum

class Type(Enum):
    INT = 0
    FLOAT = 1
    CHAR = 2
    VOID = 3
    ID = 4

class Level(Enum):
    PUBLIC = 0
    PRIVATE = 1

class UserClass:
    def __init__(self, name, parent = None):
        self.name = name
        self.methods = DirFunc()
        self.attributes = dict()
        self.parent = parent

    def __repr__(self):
        return f'\nClass\n \tName: {self.name}\n \tParent: {self.parent}\n \tAttributes: {self.attributes}\n \tMethods{self.methods}'

    def set_data_from_parent(self, parent):
        for (var_name, var_obj) in parent.attributes.items():
            self.attributes[var_name] = var_obj
        
        for (method_name, method_obj) in parent.methods.table.items():
            self.methods.table[method_name] = method_obj

    def set_parent(self, parent):
        self.parent = parent.name
        self.set_data_from_parent(parent)

class Function:
    def __init__(self, name, return_type = Type.VOID, level = Level.PUBLIC, original_class = None):
        self.name = name
        self.level = level
        self.return_type = return_type
        self.original_class = original_class
        self.variables = dict()

    def __repr__(self):
        return f'\nFunction\n \tName: {self.name}\n \tLevel: {self.level}\n \tReturn Type: {self.return_type}\n \tOriginal Class: {self.original_class}\n \tVariables{self.variables}\n'
    
class Variable:
    def __init__(self, name, type, type_id = None, level = Level.PUBLIC, original_class = None):
        self.name = name
        self.type = type
        if self.type == Type.ID:
            self.type_id = type_id
        else:
            self.type_id = None
        self.level = level
        self.original_class = original_class
        
    def __repr__(self):
        return f'\tVariable Name: {self.name} Level: {self.level} Type: {self.type} Original Class: {self.original_class}\n'

class DirFunc:
    def __init__(self):
        self.table = dict()

    def __repr__(self):
        return f"DirFunc: {self.table}"

    def add(self, function):
        self.table[function.name] = function

class DirClass:
    def __init__(self):
        self.table = dict()
    
    def __repr__(self):
        return f"DirClass: {self.table}" 

    def add(self, userClass):
        self.table[userClass.name] = userClass

class DirGen(TeamPlusPlusListener):
    def __init__(self):
        self.dir_func = DirFunc()
        self.dir_class = DirClass()
        self.current_scope = ""
        self.current_class = ""
        self.current_type = None
        self.current_type_id = ""
        self.current_level = ""
        self.in_class = 0
        self.in_function = 0

    def __repr__(self):
        return f"{self.dir_func} \n {self.dir_class}"

    def function_exists(self, function_name, class_name = None):            
        # Search only in the main function directory
        if self.in_class == 0:
            if function_name in self.dir_func.table.keys():
                return True
            return False

        # Search in the directories of the class and all of its ancestors.
        if self.in_class == 1:
            class_obj = self.dir_class.table[class_name]
            if function_name in class_obj.methods.table.keys():
                return True
            return False

    def add_function(self, function_name, class_name = None, function_type = Type.VOID, function_level = Level.PUBLIC):
        self.current_scope = function_name

        if self.function_exists(function_name, class_name):
            raise Exception(f'Function \'{function_name}\' already declared.')
        
        if self.in_class == 0:
            self.dir_func.add(Function(function_name, function_type, function_level))
        else:
            self.dir_class.table[class_name].methods.add(Function(function_name, function_type, function_level, class_name))
    
            
    def variable_exists(self, variable_name, class_name = None):

        def attribute_search(variable_name, class_name):
            class_obj = self.dir_class.table[class_name]
            if variable_name in class_obj.attributes.keys():
                return True
            if class_obj.parent is not None:
                return attribute_search(variable_name, class_obj.parent)
            return False

        # Search outside of classes
        if self.in_class == 0:
            if variable_name in self.dir_func.table[self.current_scope].variables.keys() or variable_name in self.dir_func.table['global'].variables.keys():
                return True
            return False
        
        # Search inside classes
        if self.in_class == 1:
            if self.current_scope == self.current_class: # Variable is an attribute
                return attribute_search(variable_name, class_name)
            else: # Variable is local to a method
                if variable_name in self.dir_class.table[self.current_class].methods.table[self.current_scope].variables.keys():
                    return True
                return attribute_search(variable_name, class_name)

    
    # Point 1
    def enterProgram(self, ctx):
        self.add_function('global')
        
    # Point 9 
    def enterClasses(self, ctx):
        self.in_class = 1
        
    # Point 11
    def exitClasses(self, ctx):
        self.in_class = 0
        self.current_level = Level.PUBLIC
        self.current_scope = 'global'
        
    # Point 2
    def enterTpp_class(self, ctx):
        self.current_scope = ctx.ID().getText()
        self.current_class = self.current_scope

        if self.current_scope in self.dir_class.table.keys():
            raise Exception(f'Class \'{self.current_scope}\' already declared.')
        
        self.dir_class.add(UserClass(self.current_scope))
        
    # Point 3
    def exitInherit(self, ctx):
        parent_name = ctx.ID().getText()
        if not parent_name in self.dir_class.table.keys():
            raise Exception(f'Class \'{self.current_scope}\' inherits from undeclared class \'{parent_name}\'.')
        
        current_class = self.dir_class.table[self.current_scope]
        parent_obj = self.dir_class.table[parent_name]
        current_class.set_parent(parent_obj)
            
    # Point 6
    def exitId_type(self, ctx):
        if not ctx.ID().getText() in self.dir_class.table.keys():
            raise Exception(f'Class \'{ctx.ID().getText()}\' is undefined.')
        
        self.current_type = Type.ID
        self.current_type_id = ctx.ID().getText()
        
    # Point 7
    def enterInit(self, ctx):
        variable_name = ctx.ID().getText()

        if self.variable_exists(variable_name, self.current_class):
            raise Exception(f'Variable \'{variable_name}\' already declared.')
        
        if self.in_class == 0: # Variable out of classes
            self.dir_func.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
        elif self.in_function == 0: # Variable is an attribute
            self.dir_class.table[self.current_class].attributes[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level, self.current_class)
        else: # Variable is local to a method
            self.dir_class.table[self.current_class].methods.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)

    # Point 5
    def exitVoid_type(self, ctx):
        self.current_type = Type.VOID
    
    # Point 12
    def enterDeclare_func(self, ctx):
        self.in_function = 1
    
    # Point 8
    def exitDeclare_func(self, ctx):
        self.add_function(ctx.ID().getText(), self.current_class, self.current_type, self.current_level)
        
    # Point 7
    def exitParam(self, ctx):
        variable_name = ctx.ID().getText()

        if self.variable_exists(variable_name, self.current_class):
            raise Exception(f'Variable \'{variable_name}\' already declared.')
        
        if self.in_class == 0: # Variable out of classes
            self.dir_func.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
        else: # Variable is local to a method
            self.dir_class.table[self.current_class].methods.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
    
    # Point 13
    def exitFunblock(self, ctx):
        self.in_function = 0

    # Point 10
    def enterMain(self, ctx):
        self.add_function('main')
    
    # Point 5
    def exitTpp_type(self, ctx):
        if ctx.INT() is not None:
            self.current_type = Type.INT
        elif ctx.FLOAT() is not None:
            self.current_type = Type.FLOAT
        elif ctx.CHAR() is not None: 
            self.current_type = Type.CHAR
        else:
            raise Exception(f'Type \'{ctx.getStart().getText()}\' is invalid.')

    # Point 4
    def exitLevel(self, ctx):
        if ctx.PUBLIC() is not None:
            self.current_level = Level.PUBLIC
        elif ctx.PRIVATE() is not None:
            self.current_level = Level.PRIVATE
        else:
            raise Exception(f'Level \'{ctx.getStart().getText()}\' is invalid.')