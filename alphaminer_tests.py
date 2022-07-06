from cProfile import run
import unittest

#Step 1
import alphaminer

# class TestDict(unittest.TestCase):
#     def test_init(self):
#         inputs = [a]
#         expected_outputs = [a]
#         d = TL(a, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict)) 

class Test_Alpha(unittest.TestCase):
    def test_step_1(self):
        result = alphaminer.TL(['a', 'e', 'd'], ['a', 'c', 'b', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'c', 'b', 'd'])
        self.assertEqual(result,['e', 'd', 'a', 'b', 'c'])
        


if __name__ == "__main__":
    unittest.main()
    


