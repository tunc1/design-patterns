from unittest import TestCase
from adapter import Robot,RobotAdapter

class AdapterTest(TestCase):
    
    def test_hello(self):
        robot=Robot()
        person=RobotAdapter(robot)
        self.assertEqual(person.hello(),robot.make_noise())