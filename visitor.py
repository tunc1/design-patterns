from abc import ABC,abstractmethod

class Visitable(ABC):
    
    @abstractmethod
    def accept(self,visitor):
        pass

class Entity(Visitable):
    
    def __init__(self,id=0,name=None):
        self.id=id
        self.name=name
    
    def accept(self,visitor):
        visitor.visit(self)

class Visitor(ABC):
    
    @abstractmethod
    def visit(self,visitable):
        pass

class EntityRepository(Visitor):
    
    def visit(self,visitable):
        self.save_or_update(visitable)
    
    def save_or_update(self,entity):
        if entity.id==0:
            entity.id=1