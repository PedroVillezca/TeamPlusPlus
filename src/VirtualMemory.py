import sys
from util.Enums import Type

class AddressManager:
    def __init__(self, context):
        self.context = context

        self.addresses = {
            Type.INT: 0,
            Type.FLOAT: 0,
            Type.CHAR: 0
        }
    
    def get_address(self, type, d1 = None, d2 = None):
        d1 = 0 if d1 is None else d1
        d2 = 1 if d2 is None else d2

        amount = (1 if d1*d2 == 0 else d1*d2)
        if type == Type.ID or type == Type.VOID:
            print(f"[Error] Cannot get address for variable of type \'{Type(type).name}\'.")
            sys.exit()
        
        if self.addresses[type] + amount > 100:
            print(f"[Error] Address limit for variables of type \'{Type(type).name}\' exceeded in current context.")
            sys.exit()

        context_val = self.context * 1000

        if type == Type.INT:
            type_val = 0
        elif type == Type.FLOAT:
            type_val = 100
        else:
            type_val = 200
        
        address_val = self.addresses[type]
        self.addresses[type] += amount

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

        self.free_addresses = {
            Type.INT: [],
            Type.FLOAT: [],
            Type.CHAR: []
        }

    def get_address(self, type):
        if not self.free_addresses[type]:
            # Return newly generated address
            return super().get_address(type)
            
        # Return recycled address
        return self.free_addresses[type].pop(0)
        
    def return_address(self, address):
        if address // 100 == 20:
            # Address is an INT
            self.free_addresses[Type.INT].append(address)
        elif address // 100 == 21:
            # Address is a FLOAT
            self.free_addresses[Type.FLOAT].append(address)
        elif address // 100 == 22:
            # Address is a CHAR
            self.free_addresses[Type.CHAR].append(address)

class ConstAddressManager(AddressManager):
    def __init__(self):
        super().__init__(3)

        self.const_table = {
            Type.INT: {},
            Type.FLOAT: {},
            Type.CHAR: {}
        }
    
    def get_address(self, type, value):
        if value in self.const_table[type].keys():
            # Return previously assigned address for this value
            return self.const_table[type][value]
        
        # Assign new address to unseen constant
        address = super().get_address(type)
        self.const_table[type][value] = address
        return address
            
class FunctionAddressManager():
    def __init__(self):
        self.local = LocalAddressManager()
        self.temp = TempAddressManager()
    
    def get_local_address(self, type, d1, d2):
        return self.local.get_address(type, d1, d2)
    
    def get_temp_address(self, type):
        return self.temp.get_address(type)
    
    def return_temp_address(self, address):
        return self.temp.return_address(address)

    def get_size(self):
        return self.local.get_size() + self.temp.get_size()

    def __repr__(self):
        return f"Local: \n\t{self.local} \n \tTemp: \n\t{self.temp}"

class PointerManager():
    def __init__(self):
        self.addresses = 6000
    
    def get_pointer(self):
        self.addresses += 1
        return self.addresses - 1