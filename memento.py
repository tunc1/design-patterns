class Model:
    
    def __init__(self,data):
        self.data=data
    
    def save(self):
        return Memento(self.data)
    
    def restore(self,memento):
        self.data=memento.data

class Memento:
    
    def __init__(self,data):
        self.data=data

class Caretaker():
    
    def __init__(self):
        self.__mementos=[]

    def add(self,memento):
        self.__mementos.append(memento)

    def get(self,index):
        return self.__mementos[index]