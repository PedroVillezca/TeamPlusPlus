from util.Enums import Type

class AddressManager:
    def __init__(self, context):
        self.context = context

        self.addresses = {
            Type.INT: 0,
            Type.FLOAT: 0,
            Type.CHAR: 0
        }
    
    def get_address(self, type):
        if type == Type.ID or type == Type.VOID:
            raise Exception(f"Can't get address for variable of type \'{Type(type).name}\'.")
        
        if self.addresses[type] > 99:
            raise Exception(f"Address limit for variable of type \'{Type(type).name}\' exceeded in current context.")
        
        context_val = self.context * 1000

        if type == Type.INT:
            type_val = 0
        elif type == Type.FLOAT:
            type_val = 100
        else:
            type_val = 200
        
        address_val = self.addresses[type]
        self.addresses[type] += 1

        return context_val + type_val + address_val

    def get_size(self):
        return sum(self.addresses.values())

    def __repr__(self):
        return f"Context: {self.context} Addresses: {self.addresses.values()}"

class GlobalAddressManager(AddressManager):
    def __init__(self):
        super().__init__(0)

class LocalAddressManager(AddressManager):
    def __init__(self):
        super().__init__(1)

class TempAddressManager(AddressManager):
    def __init__(self):
        super().__init__(2)

    # Add recycling address process
    
class FunctionAddressManager():
    def __init__(self):
        self.local = LocalAddressManager()
        self.temp = TempAddressManager()
    
    def get_local_address(self, type):
        return self.local.get_address(type)
    
    def get_temp_address(self, type):
        return self.temp.get_address(type)

    def get_size(self):
        return self.local.get_size() + self.temp.get_size()

    def __repr__(self):
        return f"Local: \n\t{self.local} \n \tTemp: \n\t{self.temp}"


"""
global = 0
    int
    float
    char

local 1
    int
    float
    char

temp 2
    int
    float
    char

classes*

const 3
    int
    float
    char

"""

class SizeTemplate:
    def __init__(self):
        self.local = {
            Type.INT: 0,
            Type.FLOAT: 0,
            Type.CHAR: 0
        }

        self.temp = {
            Type.INT: 0,
            Type.FLOAT: 0,
            Type.CHAR: 0
        }

    def add_local(self, type):
        if type != Type.ID and type != Type.VOID:
            self.local[type] += 1

    def add_temp(self, type):
        if type != Type.ID and type != Type.VOID:
            self.temp[type] += 1

    def get_size(self):
        return sum(self.local.values()) + sum(self.temp.values())

    def __repr__(self):
        return f"Local: {self.local.values()} \n \tTemp: {self.temp.values()}"

    
