from abc import ABC,abstractmethod
from getpass import getpass

class SignIn(ABC):
    
    def sign_in(self):
        username=self.get_username()
        password=self.get_password()
        return self.check(username,password)

    def get_username(self):
        return input("Enter username: ")

    def get_password(self):
        return getpass("Enter password: ")
    
    @abstractmethod
    def check(self,username,password):
        pass

class GithubSignIn(SignIn):
    
    def check(self,username,password):
        print("Checking password and username for github")
        return username=="github" and password=="password"

class TwitterSignIn(SignIn):
    
    def check(self,username,password):
        print("Checking password and username for twitter")
        return username=="twitter" and password=="password"