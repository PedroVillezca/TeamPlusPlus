import sys
from util.Enums import Type

class AddressManager:
    """
    Defines the logic to hand out virtual addresses based on context and
    data type. 
    """

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

        # Get total size based on calculated dimensions
        amount = (1 if d1*d2 == 0 else d1*d2)

        if type == Type.ID or type == Type.VOID:
            print(f"[Error] Cannot get address for variable of type \'{Type(type).name}\'.")
            sys.exit()
        
        if self.addresses[type] + amount > 100:
            print(f"[Error] Address limit for variables of type \'{Type(type).name}\' exceeded in current context.")
            sys.exit()

        # Get value based on context
        context_val = self.context * 1000

        # Get value based on data type
        if type == Type.INT:
            type_val = 0
        elif type == Type.FLOAT:
            type_val = 100
        else:
            type_val = 200
        
        # Get next address counter for requested type
        address_val = self.addresses[type]
        self.addresses[type] += amount

        # Return resulting address
        return context_val + type_val + address_val

    def get_size(self):
        return sum(self.addresses.values())

    def __repr__(self):
        return f"Context: {self.context} Addresses: {self.addresses.values()}"

class GlobalAddressManager(AddressManager):
    """
    Inherits from AddressManager, assigns context to 0.
    """

    def __init__(self):
        super().__init__(0)

class LocalAddressManager(AddressManager):
    """
    Inherits from AddressManager, assigns context to 1.
    """

    def __init__(self):
        super().__init__(1)

class TempAddressManager(AddressManager):
    """
    Inherits from AddressManager, assigns context to 2. Adds additional logic to
    recycle temporal addresses.
    """

    def __init__(self):
        super().__init__(2)

        self.free_addresses = {
            Type.INT: [],
            Type.FLOAT: [],
            Type.CHAR: []
        }

    def get_address(self, type):
        if type == Type.VOID:
            return None
            
        if not self.free_addresses[type]:
            # Return newly generated address
            return super().get_address(type)
            
        # Return recycled address
        return self.free_addresses[type].pop(0)
        
    def return_address(self, address):
        if address // 100 == 20:
            # Address is for an INT
            self.free_addresses[Type.INT].append(address)
        elif address // 100 == 21:
            # Address is for a FLOAT
            self.free_addresses[Type.FLOAT].append(address)
        elif address // 100 == 22:
            # Address is for a CHAR
            self.free_addresses[Type.CHAR].append(address)

class PointerManager():
    """
    Implements the logic to hand out pointer addresses. These are not separated by type,
    there is just a single counter.
    """

    def __init__(self):
        self.addresses = 4000
    
    def get_pointer(self):
        if self.addresses + 1 > 5000:
            print("[Error] Address limit for pointers exceeded in current context.")
            sys.exit()

        # Get next address counter
        self.addresses += 1
        return self.addresses - 1
            
class FunctionAddressManager():
    """
    Implements the structure to handle virtual memory required for functions.
    Includes a different Address Manager to handle local, temporal, pointer, and
    instance memory.
    """

    def __init__(self):
        self.local = LocalAddressManager()
        self.temp = TempAddressManager()
        self.pointer = PointerManager()
        self.instance = LocalInstanceManager()

    def get_address(self, type, d1, d2):
        if type != Type.ID:
            # Get address for local variable
            return self.local.get_address(type, d1, d2)

        # Get address for an instance
        return self.instance.get_address(d1, d2)
    
    def get_temp_address(self, type):
        return self.temp.get_address(type)
    
    def return_temp_address(self, address):
        return self.temp.return_address(address)

    def get_pointer(self):
        return self.pointer.get_pointer()

    def get_size(self):
        return self.local.get_size() + self.temp.get_size()

    def __repr__(self):
        return f"Local: \n\t{self.local} \n \tTemp: \n\t{self.temp}"

class ConstAddressManager(AddressManager):
    """
    Inherits from AddressManager, assigns context to 3. Adds aditional structure to
    save and recycle addresses for constants.
    """

    def __init__(self):
        super().__init__(3)

        self.const_table = {
            Type.INT: {},
            Type.FLOAT: {},
            Type.CHAR: {}
        }
    
    def get_address(self, type, value):
        if value in self.const_table[type].keys():
            # Return previously assigned address for this constant
            return self.const_table[type][value]
        
        # Assign new address to unseen constant
        address = super().get_address(type)
        self.const_table[type][value] = address
        return address

class AttributeAddressManager(AddressManager):
    """
    Inherits from AddressManager, assigns context to 7.
    """

    def __init__(self):
        super().__init__(7)

class LocalInstanceManager():
    """
    Defines the address manager to handle local instances. Similar to PointerManager,
    handles only a single list. Assigns context to 5.
    """

    def __init__(self):
        self.addresses = 5000
    
    def get_address(self, d1, d2):
        d1 = 0 if d1 is None else d1
        d2 = 1 if d2 is None else d2

        # Get total size based on calculated dimensions
        amount = (1 if d1*d2 == 0 else d1*d2)

        if self.addresses + amount > 6000:
            print("[Error] Address limit for instances exceeded in current context.")
            sys.exit()
        
        # Get next address counter for local instance, update it based on the amount requested
        address = self.addresses
        self.addresses += amount
        return address

class GlobalInstanceManager():
    """
    Defines the address manager to handle global instances, very similar to 
    LocalInstanceManager, but assigns context to 6.
    """

    def __init__(self):
        self.addresses = 6000
    
    def get_address(self, d1, d2):
        d1 = 0 if d1 is None else d1
        d2 = 1 if d2 is None else d2

        # Get total size based on calculated dimensions
        amount = (1 if d1*d2 == 0 else d1*d2)

        if self.addresses + amount > 7000:
            print("[Error] Address limit for instances exceeded in current context.")
            sys.exit()
        
        # Get next address counter for global instance, update it based on the amount requested
        address = self.addresses
        self.addresses += amount
        return address