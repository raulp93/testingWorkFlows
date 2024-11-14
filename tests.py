import unittest
from task import myFunc


class TestMyFunc(unittest.TestCase):

    def test1(self):
        expected = "Hello World"
        self.assertEqual(myFunc(), expected)

    def test2(self):
        expected = "Hola World"
        self.assertEqual(myFunc(), expected)


if __name__ == "__main__":
    unittest.main()
