from unittest import TestCase
from proxy import RepositoryProxy,Repository
from unittest.mock import Mock

class ProxyTest(TestCase):

    def test_get(self):
        repository=Repository()
        repository_mock=Mock()
        repository_mock.get.return_value=repository.get()
        repository_proxy=RepositoryProxy(repository_mock)
        self.assertEqual(repository_proxy.get(),repository.get())
        self.assertEqual(repository_proxy.get(),repository.get())
        repository_mock.get.assert_called_once()