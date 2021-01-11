class Singleton:
    __instance=None
    __hasInstanceRunned=False
    
    def __new__(cls):
        if (not Singleton.__hasInstanceRunned) or (Singleton.__instance!=None):
            raise RuntimeError
        return super(Singleton,cls).__new__(cls)
    
    @staticmethod
    def instance():
        Singleton.__hasInstanceRunned=True
        if Singleton.__instance==None:
            Singleton.__instance=Singleton()
        return Singleton.__instance