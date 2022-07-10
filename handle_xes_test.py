import unittest
from handle_xes import handle_test


class TEST_handle_test(unittest.TestCase):
    def test_handle_test(self):
        result = handle_test("datasets/L1.xes")
        self.assertEqual(result, [['a', 'e', 'd'], ['a', 'c', 'b', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'c', 'b', 'd']])

    

if __name__ == '__main__':
    unittest.main()

