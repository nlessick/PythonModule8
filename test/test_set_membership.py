import unittest
from more_fun_with_collections.set_membership import in_set


class test_set_one(unittest.TestCase):
    def test_in_set_true(self):
        test_set = {0,3,5}
        test_true = in_set(test_set)
        self.assertEqual(test_true,('Does the set contact 3? ', True))

    def test_in_set_false(self):
        test_set = {1,4,7}
        test_false = in_set(test_set)
        self.assertEqual(test_false,('Does the set contact 3? ', False))


if __name__ == '__main__':
    unittest.main()
