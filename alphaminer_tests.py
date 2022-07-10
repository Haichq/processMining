# class Test_Alpha(unittest.TestCase):
#     def test_step_1(self):
#         result = alphaminer.TL(['a', 'e', 'd'], ['a', 'c', 'b', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'c', 'b', 'd'])
#         self.assertEqual(result,['e', 'd', 'a', 'b', 'c'])


from cProfile import run
import unittest
from handle_xes import handle_test
from alphaminer import test_data
import alphaminer

class Test_Alpha(unittest.TestCase):
    def test_step_1(self):
        result = handle_test("datasets/L1.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a'})
        self.assertEqual(TO, {'d'})
        self.assertEqual(TL, {'d', 'e', 'a', 'c', 'b'})
        checkYL = {
            (frozenset({"a"}), frozenset({"e", "b"})),
            (frozenset({"e", "b"}), frozenset({"d"})),
            (frozenset({"a"}), frozenset({"e", "c"})),
            (frozenset({"e", "c"}), frozenset({"d"}))
        }
        checkXL = {
            (frozenset({"a"}), frozenset({"e"})),
            (frozenset({"a"}), frozenset({"b"})),
            (frozenset({"e"}), frozenset({"d"})),
            (frozenset({"a"}), frozenset({"e", "c"})),
            (frozenset({"e", "c"}), frozenset({"d"})),
            (frozenset({"a"}), frozenset({"c"})),
            (frozenset({"b", "e"}), frozenset({"d"})),
            (frozenset({"b"}), frozenset({"d"})),
            (frozenset({"a"}), frozenset({"b", "e"})),
            (frozenset({"c"}), frozenset({"d"})),
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    #L2
    # def test_step_1(self):
    #     result = handle_test("datasets/L2.xes")
    #     TI, TO, TL, YL = test_data(result)
    #     self.assertEqual(TI, {'a'})
    #     self.assertEqual(TO, {'d'})
    #     self.assertEqual(TL, {'d', 'e', 'a', 'c', 'b'})
    #     checkYL = {
    #         (frozenset({"a"}), frozenset({"e", "b"})),
    #         (frozenset({"e", "b"}), frozenset({"d"})),
    #         (frozenset({"a"}), frozenset({"e", "c"})),
    #         (frozenset({"e", "c"}), frozenset({"d"}))
    #     }
    #     for i in YL:
    #         print(i, type(i))
    #     self.assertEqual(YL, checkYL)
        


if __name__ == "__main__":
    unittest.main()
    

    


