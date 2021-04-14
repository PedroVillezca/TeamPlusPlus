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

class Function:
    def __init__(self, name, return_type = Type.VOID, level = Level.PUBLIC):
        self.name = name
        self.level = level
        self.return_type = return_type
        self.variables = dict()

    def __repr__(self):
        return f'\nFunction\n \tName: {self.name}\n \tLevel: {self.level}\n \tReturn Type: {self.return_type}\n \tVariables{self.variables}'
    
class Variable:
    def __init__(self, name, type, type_id = None, level = Level.PUBLIC):
        self.name = name
        self.type = type
        if self.type == Type.ID:
            self.type_id = type_id
        else:
            self.type_id = None
        self.level = level
        
    def __repr__(self):
        return f'\tVariable Name: {self.name} Level: {self.level} Type: {self.type}'

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

    def setParent(self, className, parent):
        self.table[className].parent = parent

class DirGen(TeamPlusPlusListener):
    def __init__(self):
        self.dir_func = DirFunc()
        self.dir_class = DirClass()
        self.current_scope = ""
        self.current_class = ""
        self.current_type = None
        self.current_type_id = ""
        self.current_level = ""
        self.in_class = None

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
            if class_obj.parent is not None:
                return self.function_exists(function_name, class_obj.parent)
            return False
            
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
    def enterProgram(self, node):
        self.current_scope = 'global'

        if self.function_exists(self.current_scope):
            raise Exception(f'Function \'{self.current_scope}\' already declared.')
        
        self.dir_func.add(Function('global'))
        
    # Point 9 
    def enterClasses(self, node):
        self.in_class = 1
        
    # Point 11
    def exitClasses(self, node):
        self.in_class = 0
        self.current_level = Level.PUBLIC
        self.current_scope = 'global'
        
    # Point 2
    def enterTpp_class(self, node):
        self.current_scope = node.ID().getText()
        self.current_class = self.current_scope

        if self.current_scope in self.dir_class.table.keys():
            raise Exception(f'Class \'{self.current_scope}\' already declared.')
        
        self.dir_class.add(UserClass(self.current_scope))
        
    # Point 3
    def exitInherit(self, node):
        if not node.ID().getText() in self.dir_class.table.keys():
            raise Exception(f'Class \'{self.current_scope}\' inherits from undeclared class \'{node.ID().getText()}\'.')
        
        self.dir_class.setParent(self.current_scope, node.ID().getText())
            
    # Point 6
    def exitId_type(self, node):
        if not node.ID().getText() in self.dir_class.table.keys():
            raise Exception(f'Class \'{node.ID().getText()}\' is undefined.')
        
        self.current_type = Type.ID
        self.current_type_id = node.ID().getText()
        
    # Point 7
    def enterInit(self, node):
        variable_name = node.ID().getText()

        if self.variable_exists(variable_name, self.current_class):
            raise Exception(f'Variable \'{variable_name}\' already declared.')
        
        if self.in_class == 0: # Variable out of classes
            self.dir_func.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
        elif self.current_scope == self.current_class: # Variable is an attribute
            self.dir_class.table[self.current_class].attributes[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
        else: # Variable is local to a method
            self.dir_class.table[current_class].methods.table[current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)

    # Point 5
    def exitVoid_type(self, node):
        self.current_type = Type.VOID

    # Point 8
    def exitDeclare_func(self, node):
        self.current_scope = node.ID().getText()

        if self.function_exists(self.current_scope, self.current_class):
            raise Exception(f'Function \'{self.current_scope}\' already declared.')
        
        if self.in_class == 0:
            self.dir_func.add(Function(self.current_scope, self.current_type, self.current_level))
        else:
            self.dir_class.table[self.current_class].methods.add(Function(self.current_scope, self.current_type, self.current_level))
        
    # Point 7
    def exitParam(self, node):
        variable_name = node.ID().getText()

        if self.variable_exists(variable_name, self.current_class):
            raise Exception(f'Variable \'{variable_name}\' already declared.')
        
        if self.in_class == 0: # Variable out of classes
            self.dir_func.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
        else: # Variable is local to a method
            self.dir_class.table[self.current_class].methods.table[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, self.current_level)
    
    # Point 10
    def enterMain(self, node):
        self.current_scope = 'main'

        if self.function_exists(self.current_scope):
            raise Exception(f'Function \'{self.current_scope}\' already declared.')
        
        self.dir_func.add(Function('main'))
    
    # Point 5
    def exitTpp_type(self, node):
        if node.INT() is not None:
            self.current_type = Type.INT
        elif node.FLOAT() is not None:
            self.current_type = Type.FLOAT
        elif node.CHAR() is not None: 
            self.current_type = Type.CHAR
        else:
            raise Exception(f'Type \'{node.getStart().getText()}\' is invalid.')

    # Point 4
    def exitLevel(self, node):
        if node.PUBLIC() is not None:
            self.current_level = Level.PUBLIC
        elif node.PRIVATE() is not None:
            self.current_level = Level.PRIVATE
        else:
            raise Exception(f'Level \'{node.getStart().getText()}\' is invalid.')
        