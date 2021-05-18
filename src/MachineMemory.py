from util.Enums import Type

class FunctionMemory:
    def __init__(self, local_dir, temp_dir, return_addr, next_quad):
        self.local_memory = MachineMemory(local_dir)
        self.temp_memory = MachineMemory(temp_dir)
        self.return_addr = return_addr
        self.next_quad = next_quad
    
    def advance(self):
        self.next_quad += 1

class MachineMemory:
    def __init__(self, address_dir):
        self.memory = {
            Type.INT: [None for i in range(address_dir.addresses[Type.INT])],
            Type.FLOAT: [None for i in range(address_dir.addresses[Type.FLOAT])],
            Type.CHAR: [None for i in range(address_dir.addresses[Type.CHAR])],
        }
    
    def read_address(self, address):
        type = address // 100
        index = address % 100
        return self.memory[type][index]

    def write_address(self, address, value):
        type = address // 100
        index = address % 100
        self.memory[type][index] = value

class PointerMemory:
    def __init__(self, pointer_manager):
        self.memory = [None for i in range(pointer_manager.addresses - 6000)]

    def read_pointer(self, address):
        return self.memory[address]

    def write_pointer(self, address, value):
        self.memory[address] = value

        