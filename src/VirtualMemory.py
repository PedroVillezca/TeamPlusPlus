from util.Enums import Type

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

    
