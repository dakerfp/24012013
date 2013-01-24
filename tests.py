#encoding: utf-8

import unittest
from problem import lampadas


class TesteProblema(unittest.TestCase):


    def test_problema1(self):
        result = lampadas(1)
        self.assertEquals(["on"], result)

    def test_problema2(self):
        result = lampadas(2)
        self.assertEquals(["on","off"], result)

    def test_problema3(self):
        result = lampadas(3)
        self.assertEquals(["on", "off", "off"], result)    

    def test_problema4(self):
        result = lampadas(5)
        self.assertEquals(["on","off","off","on","off"],result)

    def test_problema5(self):
        result = lampadas(6)
        self.assertEquals(["on","off","off","on","off", "off"],result)

if __name__ == "__main__":
    unittest.main()