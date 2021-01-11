from unittest import TestCase
from composite import *

class CompositeTest(TestCase):
    
    def test_works(self):
        manager=Manager("manager")
        manager2=Manager("manager2")
        manager.add_employee(manager2)
        employee=Employee("employee")
        manager2.add_employee(employee)
        self.assertTrue(manager.works(manager2))
        self.assertTrue(manager2.works(employee))
        self.assertTrue(manager.works(employee))