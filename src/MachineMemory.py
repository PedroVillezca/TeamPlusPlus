from util.Enums import Type

class FunctionMemory:
    """
    Defines the structure that will be used to create the memory required for a function call.
    This includes a local, and temporal Machine Memory, as well as a pointer memory and an instance list.
    """

    def __init__(self, local_dir, temp_dir, pointer_dir, return_addr, next_quad, is_method = False):
        self.local_memory = MachineMemory(local_dir)
        self.temp_memory = MachineMemory(temp_dir)
        self.pointer_memory = PointerMemory(pointer_dir)
        self.return_addr = return_addr
        self.next_quad = next_quad
        self.instance_list = []
        self.is_method = is_method
    
    def advance(self):
        self.next_quad += 1

class MachineMemory:
    """
    Defined the structure that will store all values that will be used during program execution.
    Consists mainly of a dictionary where data types are the keys and the values are lists, where
    the size is given by the Address Manager recieved as a paramter.
    """

    def __init__(self, address_dir):
        # Create list based on the amount of virtual directions handed out
        self.memory = {
            Type.INT: [None for i in range(address_dir.addresses[Type.INT])],
            Type.FLOAT: [None for i in range(address_dir.addresses[Type.FLOAT])],
            Type.CHAR: [None for i in range(address_dir.addresses[Type.CHAR])],
        }
    
    def read_address(self, address):
        # Return value inside the given address
        type = address // 100
        index = address % 100
        return self.memory[type][index]

    def write_address(self, address, value):
        # Write a value to the given address
        type = address // 100
        index = address % 100
        self.memory[type][index] = value

class PointerMemory:
    """
    Defines the structure needed to store pointer values. Very similar to MachineMemory,
    but only uses a single list instead of a dictionary.
    """

    def __init__(self, pointer_manager):
        self.memory = [None for i in range(pointer_manager.addresses - 4000)]

    def read_pointer(self, address):
        # Return value inside the given address
        return self.memory[address]

    def write_pointer(self, address, value):
        # Write a value to the given address
        self.memory[address] = value

class InstanceMemory(MachineMemory):
    """
    Defines the memory structure that will be used for instances. Inherits from MachineMemory, 
    so uses the same attributes and methods, however recieves an InstanceAddressManager 
    as argument.
    """

    def __init__(self, address_dir):
        super().__init__(address_dir)