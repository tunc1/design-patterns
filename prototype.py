import copy

class Prototype:
    
    def __init__(self,name):
        self.name=name

    def clone(self):
        return copy.deepcopy(self)