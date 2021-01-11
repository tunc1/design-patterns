class Mediator:
    
    def __init__(self,plane,runway):
        self.plane=plane
        self.runway=runway
        plane.mediator=self
        runway.mediator=self
    
    def can_land(self):
        return self.runway.is_empty

class Plane:
    
    def land(self):
        if self.mediator.can_land():
            print("Plane is landing")
            return True
        else:
            print("Plane can not land")
            return False

class Runway:
    
    def __init__(self):
        self.is_empty=True