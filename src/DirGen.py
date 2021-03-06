import sys

from src.VirtualMemory import GlobalAddressManager, ConstAddressManager, GlobalInstanceManager
from util.Classes import UserClass, Function, Variable, Parameter
from util.Enums import Type, Level

class DirGen:
    """
    Implements the General Directory, which is divided in Function Directory and Class
    Directory. Stores all information related to variable, function, and class definition.
    """

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

        self.d1 = None
        self.d2 = None
        
        self.global_address_manager = GlobalAddressManager()
        self.global_instance_manager = GlobalInstanceManager()
        self.const_address_manager = ConstAddressManager()

    def __repr__(self):
        return f"{self.dir_func} \n {self.dir_class}"

    def method_search(self, function_name, class_name):
        class_obj = self.dir_class[class_name]

        # Search in class's Function Directory
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
            # New function is global
            self.dir_func[new_function.name] = new_function
        else:
            # New function is a method
            new_function.set_level(function_level)
            new_function.set_original_class(class_name)
            self.dir_class[class_name].methods[new_function.name] = new_function
    
    def attribute_search(self, variable_name, class_name):
        class_obj = self.dir_class[class_name]

        # Search in class's attribute table
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

    def variable_check(self, variable_name, class_name):
        # Search outside of classes
        if self.in_class == 0:
            if variable_name in self.dir_func[self.current_scope].variables.keys():
                return self.dir_func[self.current_scope].variables[variable_name]
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
        if self.variable_check(variable_name, class_name) is not None:
            print(f'[Error] Variable \'{variable_name}\' already declared.')
            sys.exit()

        if (self.current_scope == "global"):
            # Variable is global
            if self.current_type != Type.ID:
                # Get address for a primitve global variable
                address = self.global_address_manager.get_address(self.current_type, self.d1, self.d2)
            else:
                # Get address for a global instance
                address = self.global_instance_manager.get_address(self.d1, self.d2)
            self.dir_func["global"].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address, d1=self.d1, d2=self.d2)
        elif self.in_class == 0:
            # Variable is local to a function
            address = self.dir_func[self.current_scope].get_address(self.current_type, self.d1, self.d2)
            self.dir_func[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address, d1=self.d1, d2=self.d2)
        elif self.in_function == 0:
            # Variable is an attribute
            address = self.dir_class[class_name].get_address(self.current_type, self.d1, self.d2)
            self.dir_class[class_name].attributes[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address, variable_level, class_name, d1=self.d1, d2=self.d2)
        else:
            # Variable is local to a method
            address = self.dir_class[class_name].methods[self.current_scope].get_address(self.current_type, self.d1, self.d2)
            self.dir_class[class_name].methods[self.current_scope].variables[variable_name] = Variable(variable_name, self.current_type, self.current_type_id, address, d1=self.d1, d2=self.d2)
        
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

    def get_pointer(self):
        if self.in_class == 0:
            # Pointer belongs to a global function
            return self.dir_func[self.current_scope].get_pointer()
        else:
            # Pointer belongs to a method of a class
            return self.dir_class[self.current_class].methods[self.current_scope].get_pointer()

    # Point 1
    def enterProgram(self, ctx):
        # Add function of global context to Function Directory
        new_function = Function('global')
        self.add_function(new_function)

    # Point 2
    def enterTpp_class(self, ctx):
        # Update current scope and class to the values just seen
        self.current_scope = ctx.ID().getText()
        self.current_class = self.current_scope

        if self.current_scope in self.dir_class.keys():
            print(f'[Error] Class \'{self.current_scope}\' already declared.')
            sys.exit()
        
        # Add new class to Class Directory
        new_class = UserClass(self.current_scope)
        self.dir_class[new_class.name] = new_class
        
    # Point 3
    def exitInherit(self, ctx):
        parent_name = ctx.ID().getText()
        if not parent_name in self.dir_class.keys():
            print(f'[Error] Class \'{self.current_scope}\' inherits from undeclared class \'{parent_name}\'.')
            sys.exit()
        
        # Adds attributes and methos from parent class to child class
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
        
        # Sets current type to the object's class
        self.current_type = Type.ID
        self.current_type_id = ctx.ID().getText() 
    
    # Point 7, Point 61
    def exitInit_arr(self, ctx):
        variable_name = ctx.parentCtx.ID().getText()
        
        # Adds variable to Variable Table from current context
        self.add_variable(variable_name, self.current_class, self.current_level)

        d1 = 0 if self.d1 is None else self.d1
        d2 = 1 if self.d2 is None else self.d2

        # Sets total size according to dimensions
        size = (1 if d1*d2 == 0 else d1*d2)

        self.d1 = None
        self.d2 = None

        return self.current_type, self.current_type_id, size, self.current_scope == "global"
    
    # Point 7, Point 61, Point 62
    def exitParam(self, ctx):
        # Point 7, Point 61
        variable_name = ctx.ID().getText()

        # Adds variable to function's Variable Table
        variable_address = self.add_variable(variable_name, self.current_class)

        # Point 62
        # Adds variable to function's parameter list
        self.add_param(variable_address, self.current_class)
        
    # Point 8
    def exitDeclare_func(self, ctx):
        func_name = ctx.ID().getText()

        address = None
        if self.current_type != Type.VOID:
            if self.in_class:
                # Function is a method
                var_name = self.current_class + '_' + func_name
            else:
                # Function is global
                var_name = "global_" + func_name
            
            if var_name in self.dir_func["global"].variables.keys():
                print(f'[Error] Variable \'{var_name}\' already declared.')
                sys.exit()

            # Add global variable for function with return type different to void
            address = self.global_address_manager.get_address(self.current_type)
            self.dir_func["global"].variables[var_name] = Variable(var_name, self.current_type, self.current_type_id, address)
            
        # Adds new function to the current Function Directory
        new_function = Function(func_name, self.current_type, address)
        self.add_function(new_function, self.current_class, self.current_level)
    
    # Point 9 
    def enterClasses(self, ctx):
        self.in_class = 1
    
    # Point 10
    def enterMain(self, ctx):
        # Adds function 'main' to Function Directory
        new_function = Function('main')
        self.add_function(new_function)
        
    # Point 11
    def exitClasses(self, ctx):
        # Reset values used to handle class declarations
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

    # Point 77
    def exitFirst_dim(self, ctx):
        self.d1 = int(ctx.CTE_INT().getText())
        if self.d1 <= 0:
            print("[Error] Dimensions must be greater than zero.")
            sys.exit()

    # Point 78
    def exitSecond_dim(self, ctx):
        self.d2 = int(ctx.CTE_INT().getText())
        if self.d2 <= 0:
            print("[Error] Dimensions must be greater than zero.")
            sys.exit()
