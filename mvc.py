class Model:
    
    def __init__(self,data):
        self.data=data
    
class View:
    
    def get_input(self,message):
        return input(message)
    
    def show_message(self,message):
        print(message)

class Controller:
    
    def __init__(self,model,view):
        self.view=view
        self.model=model
        self.get_input()
    
    def get_input(self):
        input=self.view.get_input("To Update Data:u, To Show Data:s ,To Exit:e ")
        if input!="e":
            if input=="u":
                data=self.view.get_input("Enter New Data: ")
                self.model.data=data
            elif input=="s":
                self.view.show_message("Current Data:"+str(self.model.data))
            else:
                self.view.show_message("Incorrect Input")
            self.get_input()