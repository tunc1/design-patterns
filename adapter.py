class Person:
    
    def hello(self):
        return "Hello"

class Robot:

    def make_noise(self):
        return "Robot makes noise"

class RobotAdapter(Person):
    
    def __init__(self,robot):
        self.robot=robot

    def hello(self):
        return self.robot.make_noise()