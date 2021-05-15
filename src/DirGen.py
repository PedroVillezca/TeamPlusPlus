import sys

from src.VirtualMemory import GlobalAddressManager, ConstAddressManager
from util.Classes import UserClass, Function, Variable, Parameter
from util.Enums import Type, Level

class DirGen:
    def __init__(self):
        self.dir_func = dict()
        self.dir_class = dict()
        self.current_scope = ""
        self.current_class = ""
        self.current_type = None
        self.current_type_id = ""
        self.current_level = ""
        self.in_class = 0
        self.in_function = 0
        
        self.global_address_manager = GlobalAddressManager()
        self.const_address_manager = ConstAddressManager()

    def __repr__(self):
        return f"{self.dir_func} \n {self.dir_class}"

    def method_search(self, function_name, class_name):
        class_obj = self.dir_class[class_name]
        if function_name in class_obj.methods.keys():
            return class_obj.methods[function_name]
        return None

    def function_search(self, function_name, class_name = None):            
        # Search only in the main function directory
        if self.in_class == 0:
            if function_name in self.dir_func.keys():
                return self.dir_func[function_name]
            return None

        # Search in the directories of the class and all of its ancestors.
        if self.in_class == 1:
            return self.method_search(function_name, class_name)

    def add_function(self, new_function, class_name = None, function_level = None):
        self.current_scope = new_function.name

        if self.function_search(new_function.name, class_name) is not None:
            print(f'[Error] Function \'{new_function.name}\' already declared.')
            sys.exit()
        
        if self.in_class == 0:
            self.dir_func[new_function.name] = new_function
        else:
            new_function.set_level(function_level)
            new_function.set_original_class(class_name)
            self.dir_class[class_name].methods[new_function.name] = new_function
    
    def attribute_search(self, variable_name, class_name):
        class_obj = self.dir_class[class_name]
        if variable_name in class_obj.attributes.keys():
            return class_obj.attributes[variable_name]
        return None
    
    def variable_search(self, variable_name, class_name):
        # Search outside of classes
        if self.in_class == 0:
            if variable_name in self.dir_func[self.current_scope].variables.keys():
                return self.dir_func[self.current_scope].variables[variable_name]
            if variable_name in self.dir_func['global'].variables.keys():
                return self.dir_func['global'].variables[variable_name]
            return None
        
        # Search inside classes
        if self.in_class == 1:
            if self.in_function == 0:
                # Variable is an attribute
                return self.attribute_search(variable_name, class_name)
            else:
                # Variable is local to a method
                if variable_name in self.dir_class[class_name].methods[self.current_scope].variables.keys():
                    return self.dir_class[class_name].methods[self.current_scope].variables[variable_name]
                return self.attribute_search(variable_name, class_name)
    
    def add_variable(self, variable_name, class_name, variable_level = None):
        if self.variable_search(variable_name, class_name) is not None:
            print(f'[Error] Variable \'{variable_name}\' already declared.')
            sys.exit()

        if (self.current_scope == "global"):
            # Variable is global
            address = self.global_address_manager.get_address(self.current_type)
            self.dir_func["global"].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address)
        elif self.in_class == 0:
            # Variable is local to a function
            address = self.dir_func[self.current_scope].get_local_address(self.current_type)
            self.dir_func[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address)
        elif self.in_function == 0:
            # Variable is an attribute
            address = 9999
            self.dir_class[class_name].attributes[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address, variable_level, class_name)
        else:
            # Variable is local to a method
            address = self.dir_class[class_name].methods[self.current_scope].get_local_address(self.current_type)
            self.dir_class[class_name].methods[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address)
        
        return address

    def add_param(self, variable_address, class_name):
        if self.in_class == 0:
            # Parameter belongs to a global function
            self.dir_func[self.current_scope].add_param(variable_address, self.current_type, self.current_type_id)
        else:
            # Parameter belongs to a method in a class
            self.dir_class[class_name].methods[self.current_scope].add_param(variable_address, self.current_type, self.current_type_id)
    
    def set_first_quad(self, quadruple_count):
        if self.in_class == 0:
            # First quad for a global function
            self.dir_func[self.current_scope].set_first_quad(quadruple_count)
        else:
            # First quad for a method of a class
            self.dir_class[self.current_class].methods[self.current_scope].set_first_quad(quadruple_count)

    def get_temp_address(self, type):
        if self.in_class == 0:
            # Temp variable belongs to a global function
            return self.dir_func[self.current_scope].get_temp_address(type)
        else:
            # Temp variable belongs to a method of a class
            return self.dir_class[self.current_class].methods[self.current_scope].get_temp_address(type)

    def return_temp_address(self, address):
        if self.in_class == 0:
            # Temp variable belongs to a global function
            return self.dir_func[self.current_scope].return_temp_address(address)
        else:
            # Temp variable belongs to a method of a class
            return self.dir_class[self.current_class].methods[self.current_scope].return_temp_address(address)

    # Point 1
    def enterProgram(self, ctx):
        new_function = Function('global')
        self.add_function(new_function)

    # Point 2
    def enterTpp_class(self, ctx):
        self.current_scope = ctx.ID().getText()
        self.current_class = self.current_scope

        if self.current_scope in self.dir_class.keys():
            print(f'[Error] Class \'{self.current_scope}\' already declared.')
            sys.exit()
        
        new_class = UserClass(self.current_scope)
        self.dir_class[new_class.name] = new_class
        
    # Point 3
    def exitInherit(self, ctx):
        parent_name = ctx.ID().getText()
        if not parent_name in self.dir_class.keys():
            print(f'[Error] Class \'{self.current_scope}\' inherits from undeclared class \'{parent_name}\'.')
            sys.exit()
        
        current_class = self.dir_class[self.current_scope]
        parent_obj = self.dir_class[parent_name]
        current_class.set_parent(parent_obj)
    
    # Point 4
    def exitLevel(self, ctx):
        if ctx.PUBLIC() is not None:
            self.current_level = Level.PUBLIC
        elif ctx.PRIVATE() is not None:
            self.current_level = Level.PRIVATE
    
    # Point 5
    def exitTpp_type(self, ctx):
        if ctx.INT() is not None:
            self.current_type = Type.INT
        elif ctx.FLOAT() is not None:
            self.current_type = Type.FLOAT
        elif ctx.CHAR() is not None: 
            self.current_type = Type.CHAR
        
    # Point 5
    def exitVoid_type(self, ctx):
        self.current_type = Type.VOID

    # Point 6
    def exitId_type(self, ctx):
        if not ctx.ID().getText() in self.dir_class.keys():
           print(f'[Error] Class \'{ctx.ID().getText()}\' is undefined.')
           sys.exit()
        
        self.current_type = Type.ID
        self.current_type_id = ctx.ID().getText() 
    
    # Point 7, Point 61
    def exitInit_arr(self, ctx):
        variable_name = ctx.parentCtx.ID().getText()
        self.add_variable(variable_name, self.current_class, self.current_level)
    
    # Point 7, Point 61, Point 62
    def exitParam(self, ctx):
        # Point 7, Point 61
        variable_name = ctx.ID().getText()
        variable_address = self.add_variable(variable_name, self.current_class)

        # Point 62
        self.add_param(variable_address, self.current_class)
        
    # Point 8
    def exitDeclare_func(self, ctx):
        func_name = ctx.ID().getText()

        address = None
        if self.current_type != Type.VOID:
            if self.in_class:
                var_name = self.current_class + '_' + func_name
            else:
                var_name = "global_" + func_name
            
            address = self.global_address_manager.get_address(self.current_type)
            self.dir_func["global"].variables[var_name] = Variable(var_name, self.current_type, self.current_type_id, address)
            
        new_function = Function(func_name, self.current_type, address)
        self.add_function(new_function, self.current_class, self.current_level)
    
    # Point 9 
    def enterClasses(self, ctx):
        self.in_class = 1
    
    # Point 10
    def enterMain(self, ctx):
        new_function = Function('main')
        self.add_function(new_function)
        
    # Point 11
    def exitClasses(self, ctx):
        self.in_class = 0
        self.current_level = Level.PUBLIC
        self.current_scope = 'global'
        self.current_class = None
        
    # Point 12
    def enterDeclare_func(self, ctx):
        self.in_function = 1
        
    # Point 13
    def exitFunblock(self, ctx):
        self.in_function = 0