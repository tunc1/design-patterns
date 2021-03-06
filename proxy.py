from abc import ABC,abstractmethod

class AbstractRepository(ABC):
    
    @abstractmethod
    def get(self):
        pass

class Repository(AbstractRepository):
    
    def get(self):
        return "Data"

class RepositoryProxy(AbstractRepository):
    
    def __init__(self,repository):
        self.repository=repository
        self.data=None
    
    def get(self):
        if self.data==None:
            self.data=self.repository.get()
        return self.data