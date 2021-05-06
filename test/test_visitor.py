from unittest import TestCase
from visitor import Entity,EntityRepository

class VisitorTest(TestCase):
    
    def test_visit(self):
        entity=Entity()
        entity_repository=EntityRepository()
        entity.accept(entity_repository)
        self.assertNotEqual(entity.id,0)