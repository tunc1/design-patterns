class MouseFactory:
    
    def create(self,type):
        if type=="wired":
            return WiredMouse()
        elif type=="wireless":
            return WirelessMouse()
        else:
            return None

class WiredMouse:
    pass

class WirelessMouse:
    pass