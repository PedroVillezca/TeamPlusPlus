from antlr4 import *
from antlr.TeamPlusPlusListener import TeamPlusPlusListener
from antlr.TeamPlusPlusParser import TeamPlusPlusParser

class UserClass:
    def __init__(self, name, parent = None):
        self.name = name
        self.methods = DirFunc()
        self.attributes = dict()
        self.parent = parent

class Function:
    def __init__(self, name, return_type, level = 'public'):
        self.name = name
        self.level = level
        self.return_type = return_type
        self.variables = dict()
    
class Variable:
    def __init__(self, name, type, level = 'public'):
        self.name = name
        self.type = type
        self.level = level

class DirFunc:
    def __init__(self):
        self.table = dict()

    def __str__(self):
        return f"DirFunc: {self.table}" 

class DirClass:
    def __init__(self):
        self.table = dict()
    
    def __str__(self):
        return f"DirClass: {self.table}" 

class DirGen(TeamPlusPlusListener):
    def __init__(self):
        self.dir_func = DirFunc()
        self.dir_class = DirClass()
        self.current_scope = ""
        self.current_type = ""
        self.current_level = ""
        self.in_class = None

    def __repr__(self):
        return f"{str(self.dir_func)} \n {str(self.dir_class)}"

    def enterProgram(self, node):
        print("I entered program")
        # Point 1

    def enterClasses(self, node):
        print("I entered classes")
        # Point 9 
    
    def exitClasses(self, node):
        print("I exited classes")
        # Point 9

    def enterTpp_class(self, node):
        print("I entered Tpp_class")
        # Point 2

    def exitInherit(self, node):
        print("I exited inherit")
        # Point 3
    
    def exitId_type(self, node):
        print("I exited Id_type")
        # Point 6

    def enterInit(self, node):
        print("I entered init")
        # Point 7

    def exitVoid_type(self, node):
        print("I exited Void_type")
        # Point 5

    def exitDeclare_func(self, node):
        print("I exited declare_func")
        # Point 8
        
    def exitParam(self, node):
        print("I exited param")
        # Point 7
    
    def enterMain(self, node):
        print("I entered main")
        # Point 10
    
    def exitTpp_type(self, node):
        print("I exited Tpp_type")
        # Point 5

    def exitLevel(self, node):
        print("I exited level")
        # Point 4