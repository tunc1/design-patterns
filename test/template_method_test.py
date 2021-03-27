from unittest import TestCase
from template_method import GithubSignIn,TwitterSignIn

class GithubSignInTest(TestCase):

    def test_sign_in(self):
        sign_in=GithubSignIn()
        self.assertTrue(sign_in.sign_in("github","password"))
        self.assertFalse(sign_in.sign_in("github","pass"))
        self.assertFalse(sign_in.sign_in("git","password"))
        self.assertFalse(sign_in.sign_in("git","passwor"))

class TwitterSignInTest(TestCase):

    def test_sign_in(self):
        sign_in=TwitterSignIn()
        self.assertTrue(sign_in.sign_in("twitter","password"))
        self.assertFalse(sign_in.sign_in("twitter","pass"))
        self.assertFalse(sign_in.sign_in("tt","password"))
        self.assertFalse(sign_in.sign_in("tt","passwor"))