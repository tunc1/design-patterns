from unittest import TestCase
from proxy import Repository,RepositoryProxy
from io import StringIO
import sys

class ProxyTest(TestCase):

    def test_get(self):
        repositoryProxy=RepositoryProxy(Repository())
        stringIO=StringIO()
        sys.stdout=stringIO
        repositoryProxy.get()
        self.assertEquals(stringIO.getvalue(),"fetching from db\n")
        repositoryProxy.get()
        self.assertEquals(stringIO.getvalue(),"fetching from db\nfetching from proxy\n")