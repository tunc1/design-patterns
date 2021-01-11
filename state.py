from abc import ABC,abstractmethod

class CellPhone:
    
    def __init__(self,wifi_state):
        self.wifi_state=wifi_state
    
    def can_connect(self):
        return self.wifi_state.can_connect()

class State(ABC):
    
    @abstractmethod
    def can_connect(self):
        pass

class WifiTurnedOnState(State):
    
    def can_connect(self):
        return True

class WifiTurnedOffState(State):
    
    def can_connect(self):
        return False