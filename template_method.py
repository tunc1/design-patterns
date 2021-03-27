from abc import ABC,abstractmethod
import getpass

class SignIn(ABC):
    
    def sign_in(self,username,password):
        if self.check(username,password):
            return True
        else:
            return False
    
    @abstractmethod
    def check(self,username,password):
        pass

class GithubSignIn(SignIn):
    
    def check(self,username,password):
        print("Checking password and username for github")
        if username=="github" and password=="password":
            return True
        return False

class TwitterSignIn(SignIn):
    
    def check(self,username,password):
        print("Checking password and username for twitter")
        if username=="twitter" and password=="password":
            return True
        return False