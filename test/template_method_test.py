from unittest import TestCase
from template_method import GithubSignIn,TwitterSignIn

class GithubSignInTest(TestCase):

    def test_check(self):
        sign_in=GithubSignIn()
        self.assertTrue(sign_in.check("github","password"))
        self.assertFalse(sign_in.check("github","pass"))
        self.assertFalse(sign_in.check("git","password"))
        self.assertFalse(sign_in.check("git","passwor"))

class TwitterSignInTest(TestCase):

    def test_check(self):
        sign_in=TwitterSignIn()
        self.assertTrue(sign_in.check("twitter","password"))
        self.assertFalse(sign_in.check("twitter","pass"))
        self.assertFalse(sign_in.check("tt","password"))
        self.assertFalse(sign_in.check("tt","passwor"))