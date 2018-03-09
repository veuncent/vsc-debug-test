import unittest
from service import SomeService

class TestSomeService(unittest.TestCase):

    def testSomeService(self):

        someService = SomeService()

        self.assertEqual(42, someService.doSomething())