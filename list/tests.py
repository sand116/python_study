import unittest
import 01


class MyTest(unittest.TestCase):
     
    def test_input_cnt(self):
        c = 01.input_cnt(20, 10)
        self.assertEqual(c, 30)
 
    def test_input_list(self):
        c = 01.input_list(20, 10)
        self.assertEqual(c, 10)
 
if __name__ == '__main__':
    unittest.main() #test method 실행
