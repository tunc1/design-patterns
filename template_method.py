from abc import ABC,abstractmethod

class SignIn(ABC):
    
    def sign_in(self,username,password):
        return self.check(username,password)
    
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