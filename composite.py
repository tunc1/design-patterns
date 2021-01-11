class Employee:
    
    def __init__(self,name):
        self.name=name

class Manager(Employee):
    
    def __init__(self,name):
        super().__init__(name)
        self.__employees=[]
    
    def add_employee(self,employee):
        self.__employees.append(employee)
    
    def delete_employee(self,employee):
        self.__employees.remove(employee)
    
    def get_employees(self):
        return self.__employees
    
    def works(self,employee):
        for item in self.__employees:
            if type(item)==Manager:
                if item==employee:
                    return True
                else:
                    return item.works(employee)
            else:
                if item==employee:
                    return True
            return False