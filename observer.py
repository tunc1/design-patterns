class Observable():
    def __init__(self):
        self.__observers=[]
    
    def addObserver(self,observer):
        self.__observers.append(observer)
    
    def deleteObserver(self,observer):
        self.__observers.remove(observer)
    
    def deleteObservers(self):
        for observer in self.__observers:
            self.deleteObserver(observer)
    
    def updateObservers(self,data):
        for observer in self.__observers:
            observer.update(data)

class Observer():
    def __init__(self,data):
        self.data=data
    
    def update(self,data):
        self.data=data