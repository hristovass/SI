import unittest
from my_module.my_module import add, subtract

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(2, 2), 0)

if __name__ == '__main__':
    unittest.main()
