class LCDScreen:
    pass

class LEDScreen:
    pass

class ScreenFactory:
    
    def __init__(self):
        self.__objects=[]
        self.__keys=[]
    
    def create(self,screen_type):
        try:
            index=self.__keys.index(screen_type)
            return self.__objects[index]
        except:
            if screen_type=="led":
                screen=LEDScreen()
            elif screen_type=="lcd":
                screen=LCDScreen()
            self.__objects.append(screen)
            self.__keys.append(screen_type)
            return screen

class TV:
    
    def __init__(self,screen):
        self.screen=screen