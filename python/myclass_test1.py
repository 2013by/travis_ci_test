'''
Created on 2017-6-19

@author: lizhu
'''
import unittest 
from mytest import Mytest
class TestMytest(unittest.TestCase):
    def setUp(self): 
       self.mytest1=Mytest()
    def tearDown(self):
        pass
    def test_function1(self):
        self.mytest1.function1()
    def test_function2(self):
        self.mytest1.function2(1,2)
    def test_function3(self):
        self.assertEquals(self.mytest1.function3(1, 3), 4, "fail")
if __name__=="__main__":
    unittest.main()