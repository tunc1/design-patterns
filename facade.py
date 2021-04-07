class Computer:

    def __init__(self):
        self.cpu=CPU()
        self.hdd=HDD()
    
    def turn_on(self):
        self.cpu.has_electricity=True
        self.hdd.start_turning()

class CPU:

    def __init__(self):
        self.has_electricity=False

class HDD:

    def __init__(self):
        self.is_turning=False
    
    def start_turning(self):
        self.is_turning=True