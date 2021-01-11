from abc import ABC,abstractmethod

class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass

class TurnOnCommand(Command):

    def __init__(self,turn_onable):
        self.turn_onable=turn_onable

    def execute(self):
        self.turn_onable.turn_on()

class TurnOffCommand(Command):

    def __init__(self,turn_offable):
        self.turn_offable=turn_offable

    def execute(self):
        self.turn_offable.turn_off()

class Remote:
    
    def __init__(self,tv):
        self.turn_on_command=TurnOnCommand(tv)
        self.turn_off_command=TurnOffCommand(tv)

    def turn_on(self):
        self.turn_on_command.execute()
    
    def turn_off(self):
        self.turn_off_command.execute()
    
class TurnOnable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
class TurnOffable(ABC):
    @abstractmethod
    def turn_off(self):
        pass

class TV(TurnOnable,TurnOffable):
    
    def __init__(self):
        self.is_on=False

    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False