from unittest import TestCase
from memento import Model,Caretaker

class MementoTest(TestCase):
    
    def test_restore(self):
        model=Model("data")
        memento=model.save()
        caretaker=Caretaker()
        caretaker.add(memento)
        model.data="data2"
        memento2=caretaker.get(0)
        model.restore(memento2)
        self.assertEqual(model.data,memento2.data)