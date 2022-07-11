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
    def test_L1(self):
        result = handle_test("datasets/L1.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a'})
        self.assertEqual(TO, {'d'})
        self.assertEqual(TL, {'d', 'e', 'a', 'c', 'b'})
        checkYL = {
            (frozenset({'a'}), frozenset({'e', 'b'})),
            (frozenset({'b', 'e'}), frozenset({'d'})),
            (frozenset({'a'}), frozenset({'e', 'c'})),
            (frozenset({'e', 'c'}), frozenset({'d'}))
        }
        checkXL = {
            (frozenset({'a'}), frozenset({'e'})),
            (frozenset({'a'}), frozenset({'b'})),
            (frozenset({'e'}), frozenset({'d'})),
            (frozenset({'a'}), frozenset({'e', 'c'})),
            (frozenset({'e', 'c'}), frozenset({'d'})),
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'b', 'e'}), frozenset({'d'})),
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'a'}), frozenset({'b', 'e'})),
            (frozenset({'c'}), frozenset({'d'})),
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_L2(self):
        result = handle_test("datasets/L2.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a'})
        self.assertEqual(TO, {'d'})
        self.assertEqual(TL, {'f','b','c','d','a','e'})
        checkXL = {
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'a'}), frozenset({'b'})),
            (frozenset({'f'}), frozenset({'c'})),
            (frozenset({'f'}), frozenset({'b'})),
            (frozenset({'c'}), frozenset({'d'})),
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'c'}), frozenset({'e'})),
            (frozenset({'b'}), frozenset({'e'})),
            (frozenset({'e'}), frozenset({'f'})),
            (frozenset({'a', 'f'}), frozenset({'c'})),
            (frozenset({'a', 'f'}), frozenset({'b'})),
            (frozenset({'c'}), frozenset({'d', 'e'})),
            (frozenset({'b'}), frozenset({'d', 'e'}))             
        }
        checkYL = {
            (frozenset({'a', 'f'}), frozenset({'c'})),
            (frozenset({'a', 'f'}), frozenset({'b'})),
            (frozenset({'c'}), frozenset({'d', 'e'})),
            (frozenset({'b'}), frozenset({'d', 'e'})),
            (frozenset({'e'}), frozenset({'f'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_L3(self):
        result = handle_test("datasets/L3.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a'})
        self.assertEqual(TO, {'g'})
        self.assertEqual(TL, {'a','b','c','d','e','f','g'})
        checkXL = {
            (frozenset({'a'}), frozenset({'b'})),
            (frozenset({'e'}), frozenset({'f'})),
            (frozenset({'f'}), frozenset({'b'})),
            (frozenset({'e'}), frozenset({'g'})),
            (frozenset({'a', 'f'}), frozenset({'b'})),
            (frozenset({'b'}), frozenset({'c'})),
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'c'}), frozenset({'e'})),
            (frozenset({'d'}), frozenset({'e'})),
            (frozenset({'e'}), frozenset({'f', 'g'}))
        }
        checkYL = {
            (frozenset({'a', 'f'}), frozenset({'b'})),
            (frozenset({'b'}), frozenset({'c'})),
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'c'}), frozenset({'e'})),
            (frozenset({'d'}), frozenset({'e'})),
            (frozenset({'e'}), frozenset({'f', 'g'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_L4(self):
        result = handle_test("datasets/L4.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a', 'b'})
        self.assertEqual(TO, {'d', 'e'})
        self.assertEqual(TL, {'a','b','c','d','e'})
        checkXL = {
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'c'}), frozenset({'d'})),
            (frozenset({'b'}), frozenset({'c'})),
            (frozenset({'c'}), frozenset({'e'})),
            (frozenset({'a', 'b'}), frozenset({'c'})),
            (frozenset({'c'}), frozenset({'d', 'e'}))              
        }
        checkYL = {
            (frozenset({'a', 'b'}), frozenset({'c'})),
            (frozenset({'c'}), frozenset({'d', 'e'})) 
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_L5(self):
        result = handle_test("datasets/L5.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a'})
        self.assertEqual(TO, {'f'})
        self.assertEqual(TL, {'a','b','c','d','e','f'})
        checkXL = {
            (frozenset({'a'}), frozenset({'e'})),
            (frozenset({'a'}), frozenset({'b'})),
            (frozenset({'d'}), frozenset({'b'})),
            (frozenset({'b'}), frozenset({'c'})),
            (frozenset({'b'}), frozenset({'f'})),
            (frozenset({'e'}), frozenset({'f'})),
            (frozenset({'c'}), frozenset({'d'})),
            (frozenset({'a', 'd'}), frozenset({'b'})),
            (frozenset({'b'}), frozenset({'c', 'f'}))              
        }
        checkYL = {
            (frozenset({'a'}), frozenset({'e'})),
            (frozenset({'a', 'd'}), frozenset({'b'})),
            (frozenset({'b'}), frozenset({'c', 'f'})),
            (frozenset({'e'}), frozenset({'f'})),
            (frozenset({'c'}), frozenset({'d'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_L6(self):
        result = handle_test("datasets/L6.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a', 'b'})
        self.assertEqual(TO, {'g'})
        self.assertEqual(TL, {'a','b','c','d','e','f','g'})
        checkXL = {
            (frozenset({'a'}), frozenset({'e'})),
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'b'}), frozenset({'f'})),
            (frozenset({'c'}), frozenset({'g'})),
            (frozenset({'d'}), frozenset({'g'})),
            (frozenset({'e'}), frozenset({'g'})),
            (frozenset({'f'}), frozenset({'g'})),
            (frozenset({'d', 'e'}), frozenset({'g'})),
            (frozenset({'c', 'd'}), frozenset({'g'})),
            (frozenset({'f', 'e'}), frozenset({'g'})),
            (frozenset({'c', 'f'}), frozenset({'g'}))
        }
        checkYL = {
            (frozenset({'a'}), frozenset({'e'})),
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'b'}), frozenset({'f'})),
            (frozenset({'d', 'e'}), frozenset({'g'})),
            (frozenset({'c', 'd'}), frozenset({'g'})),
            (frozenset({'f', 'e'}), frozenset({'g'})),
            (frozenset({'c', 'f'}), frozenset({'g'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_L7(self):
        result = handle_test("datasets/L7.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'a'})
        self.assertEqual(TO, {'c'})
        self.assertEqual(TL, {'a','b','c'})
        checkXL = {
            (frozenset({'b'}), frozenset({'c'})),
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'a'}), frozenset({'b'}))
        }
        checkYL = {
            (frozenset({'b'}), frozenset({'c'})),
            (frozenset({'a'}), frozenset({'c'})),
            (frozenset({'a'}), frozenset({'b'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_Lrenning(self):
        result = handle_test("datasets/running-example.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'register request'})
        self.assertEqual(TO, {'pay compensation','reject request'})
        self.assertEqual(TL, {'register request','check ticket','examine casually','examine thoroughly','decide','pay compensation','reject request','reinitiate request'})
        checkXL = {
            (frozenset({'register request', 'reinitiate request'}), frozenset({'check ticket'})),
            (frozenset({'register request'}), frozenset({'check ticket'})),
            (frozenset({'reinitiate request'}), frozenset({'check ticket'})),
            (frozenset({'register request','reinitiate request'}), frozenset({'examine casually','examine thoroughly'})),
            (frozenset({'register request'}), frozenset({'examine casually'})),
            (frozenset({'register request'}), frozenset({'examine thoroughly'})),
            (frozenset({'reinitiate request'}), frozenset({'examine casually'})),
            (frozenset({'reinitiate request'}), frozenset({'examine thoroughly'})),
            (frozenset({'register request', 'reinitiate request'}), frozenset({'examine casually'})),
            (frozenset({'register request', 'reinitiate request'}), frozenset({'examine thoroughly'})),
            (frozenset({'register request'}), frozenset({'examine casually','examine thoroughly'})),
            (frozenset({'reinitiate request'}), frozenset({'examine casually','examine thoroughly'})),
            (frozenset({'examine casually'}), frozenset({'decide'})),
            (frozenset({'examine thoroughly'}), frozenset({'decide'})),
            (frozenset({'examine casually','examine thoroughly'}), frozenset({'decide'})),
            (frozenset({'check ticket'}), frozenset({'decide'})),
            (frozenset({'decide'}), frozenset({'pay compensation','reject request','reinitiate request'})),
            (frozenset({'decide'}), frozenset({'pay compensation','reinitiate request'})),
            (frozenset({'decide'}), frozenset({'reject request','reinitiate request'})),
            (frozenset({'decide'}), frozenset({'pay compensation','reject request'})),
            (frozenset({'decide'}), frozenset({'pay compensation'})),
            (frozenset({'decide'}), frozenset({'reject request'})),
            (frozenset({'decide'}), frozenset({'reinitiate request'}))
        }
        checkYL = {
            (frozenset({'register request', 'reinitiate request'}), frozenset({'check ticket'})),
            (frozenset({'register request','reinitiate request'}), frozenset({'examine casually','examine thoroughly'})),
            (frozenset({'examine casually','examine thoroughly'}), frozenset({'decide'})),
            (frozenset({'check ticket'}), frozenset({'decide'})),
            (frozenset({'decide'}), frozenset({'pay compensation','reject request','reinitiate request'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_Lfly(self):
        result = handle_test("datasets/flyerinstances.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'receive flyer order'})
        self.assertEqual(TO, {'deliver flyer'})
        self.assertEqual(TL, {'receive flyer order','design flyer','send draft to customer','print flyer','deliver flyer'})
        checkXL = {
            (frozenset({'receive flyer order'}),frozenset({'design flyer'})),
            (frozenset({'send draft to customer'}),frozenset({'print flyer'})),
            (frozenset({'print flyer'}),frozenset({'deliver flyer'}))
        }
        checkYL = {
            (frozenset({'receive flyer order'}),frozenset({'design flyer'})),
            (frozenset({'send draft to customer'}),frozenset({'print flyer'})),
            (frozenset({'print flyer'}),frozenset({'deliver flyer'}))
        }
        self.assertEqual(YL, checkYL)
        self.assertEqual(XL, checkXL)

    def test_Lbil(self):
        result = handle_test("datasets/billinstances.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'write bill'})
        self.assertEqual(TO, {'deliver bill'})
        self.assertEqual(TL, {'write bill','print bill','deliver bill'})
        checkXL = {
            (frozenset({'write bill','print bill'}),frozenset({'print bill','deliver bill'}))
            }
        checkYL = {
            (frozenset({'write bill','print bill'}),frozenset({'print bill','deliver bill'}))
            }

    def test_Lpost(self):
        result = handle_test("datasets/posterinstances.xes")
        TI, TO, TL, YL, XL = test_data(result)
        self.assertEqual(TI, {'receive order and photo'})
        self.assertEqual(TO, {'deliver poster'})
        self.assertEqual(TL, {'receive order and photo','design photo poster','print poster','deliver poster'})
        checkXL = {
            (frozenset({'receive order and photo'}),frozenset({'design photo poster'})),
            (frozenset({'design photo poster'}),frozenset({'print poster'})),
            (frozenset({'print poster'}),frozenset({'deliver poster'}))
            }

        checkYL = {
            (frozenset({'receive order and photo'}),frozenset({'design photo poster'})),
            (frozenset({'design photo poster'}),frozenset({'print poster'})),
            (frozenset({'print poster'}),frozenset({'deliver poster'}))
            }


if __name__ == "__main__":
    unittest.main()
    

    


