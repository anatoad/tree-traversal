import unittest
from tree import *


class Tests(unittest.TestCase):
    def test_find_1(self):
        tree = Tree()

        tree.add(1)
        tree.add(7)
        tree.add(3)
        tree.add(4)
        tree.add(2)

        node = tree.find(4)

        assert node is not None

    def test_find_2(self):
        tree = Tree()

        tree.add(1)
        tree.add(7)
        tree.add(3)
        tree.add(4)
        tree.add(2)

        node = tree.find(5)

        assert node is None


if __name__ == '__main__':
    unittest.main()