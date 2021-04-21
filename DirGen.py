from util.Enums import Type, Level

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
    def __init__(self, name, return_type = Type.VOID, level = None, original_class = None):
        self.name = name
        self.level = level
        self.return_type = return_type
        self.original_class = original_class
        self.variables = dict()

    def __repr__(self):
        return f'\nFunction\n \tName: {self.name}\n \tLevel: {self.level}\n \tReturn Type: {self.return_type}\n \tOriginal Class: {self.original_class}\n \tVariables{self.variables}\n'
    
    def set_level(self, level):
        self.level = level

    def set_original_class(self, original_class):
        self.original_class = original_class

class Variable:
    def __init__(self, name, type, type_id = None, level = None, original_class = None):
        self.name = name
        self.type = type
        if self.type == Type.ID:
            self.type_id = type_id
        else:
            self.type_id = None
        self.level = level
        self.original_class = original_class
        
    def __repr__(self):
        return f'\tVariable Name: {self.name} Level: {self.level} Type: {self.type} Type ID: {self.type_id} Original Class: {self.original_class}\n'

    def set_level(self, level):
        self.level = level

    def set_original_class(self, original_class):
        self.original_class = original_class

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
            raise Exception(f'Function \'{new_function.name}\' already declared.')
        
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
            if self.in_function == 0: # Variable is an attribute
                return self.attribute_search(variable_name, class_name)
            else: # Variable is local to a method
                if variable_name in self.dir_class[class_name].methods[self.current_scope].variables.keys():
                    return self.dir_class[class_name].methods[self.current_scope].variables[variable_name]
                return self.attribute_search(variable_name, class_name)
    
    def add_variable(self, new_variable, class_name, variable_level = None):
        if self.variable_search(new_variable.name, class_name) is not None:
            raise Exception(f'Variable \'{new_variable.name}\' already declared.')
        
        if self.in_class == 0: # Variable out of classes
            self.dir_func[self.current_scope].variables[new_variable.name] = new_variable
        elif self.in_function == 0: # Variable is an attribute
            new_variable.set_level(variable_level)
            new_variable.set_original_class(class_name)
            self.dir_class[class_name].attributes[new_variable.name] = new_variable
        else: # Variable is local to a method
            self.dir_class[class_name].methods[self.current_scope].variables[new_variable.name] = new_variable
    
    # Point 1
    def enterProgram(self, ctx):
        new_function = Function('global')
        self.add_function(new_function)

    # Point 2
    def enterTpp_class(self, ctx):
        self.current_scope = ctx.ID().getText()
        self.current_class = self.current_scope

        if self.current_scope in self.dir_class.keys():
            raise Exception(f'Class \'{self.current_scope}\' already declared.')
        
        new_class = UserClass(self.current_scope)
        self.dir_class[new_class.name] = new_class
        
    # Point 3
    def exitInherit(self, ctx):
        parent_name = ctx.ID().getText()
        if not parent_name in self.dir_class.keys():
            raise Exception(f'Class \'{self.current_scope}\' inherits from undeclared class \'{parent_name}\'.')
        
        current_class = self.dir_class[self.current_scope]
        parent_obj = self.dir_class[parent_name]
        current_class.set_parent(parent_obj)
    
    # Point 4
    def exitLevel(self, ctx):
        if ctx.PUBLIC() is not None:
            self.current_level = Level.PUBLIC
        elif ctx.PRIVATE() is not None:
            self.current_level = Level.PRIVATE
        else:
            raise Exception(f'Level \'{ctx.getStart().getText()}\' is invalid.')
    
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
        
    # Point 5
    def exitVoid_type(self, ctx):
        self.current_type = Type.VOID

    # Point 6
    def exitId_type(self, ctx):
        if not ctx.ID().getText() in self.dir_class.keys():
           raise Exception(f'Class \'{ctx.ID().getText()}\' is undefined.')
        
        self.current_type = Type.ID
        self.current_type_id = ctx.ID().getText() 
    
    # Point 7
    def enterInit_id(self, ctx):
        variable_name = ctx.ID().getText()
        new_variable = Variable(variable_name, self.current_type, self.current_type_id)
        self.add_variable(new_variable, self.current_class, self.current_level)
    
    # Point 7
    def exitParam(self, ctx):
        variable_name = ctx.ID().getText()
        new_variable = Variable(variable_name, self.current_type, self.current_type_id)
        self.add_variable(new_variable, self.current_class)

    # Point 8
    def exitDeclare_func(self, ctx):
        new_function = Function(ctx.ID().getText(), self.current_type)
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

    