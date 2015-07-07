import unittest
import sys
sys.path.append("/home/simon_team/partition_poly")
from poly import *

class test_poly(unittest.TestCase):

    def test_add(self):
        # x^2 + y^2
        p1 = Poly({(2,0):1, (0,2):1})
        
        # xy + y^2
        p2 = Poly({(1,1):1, (0,2):1})
        
        # x^2 + xy + 2y^2
        result = {(2,0):1, (0,2):2, (1,1):1}
        
        self.assertEqual(result, (p1+p2).terms)
    
    def test_sub(self):
        # x^2 + y^2
        p1 = Poly({(2,0):1, (0,2):1})
        
        # xy + y^2
        p2 = Poly({(1,1):1, (0,2):1})
        
        # x^2 - xy
        result = {(2,0):1, (1,1):-1}
        
        self.assertEqual(result, (p1-p2).terms)
    
    def test_mul(self):
        # x^2 + y^2
        p1 = Poly({(2,0):1, (0,2):1})
        
        # xy + y^2
        p2 = Poly({(1,1):1, (0,2):1})
        
        # x^3y + xy^3 + x^2y^2 + y^4
        result = {(3,1):1, (1,3):1, (2,2):1, (0,4):1}
        
        self.assertEqual(result, (p1*p2).terms)
