import unittest
import sys
sys.path.append("/home/simon_team/partition_poly")
from poly import *
from poly import _foil2args

class test_equipSubsets(unittest.TestCase):

    def test_tup_to_dict(self):
        tup = (1,2,3)
        d = {(1,0,0):1, (0,1,0):2, (0,0,1):3}
        
        self.assertEqual(d, tupToDict(tup))
    
    def test_22(self):
        fans = [2,2]
        result1 = [(0,1),(1,0),(1,1)]
        
        result1 = [tupToDict(tup) for tup in result1]
        result2 = equipSubsets(fans)
        self.assertEqual(result1, result2)
    
    def test_33(self):
        fans = [3,3]
        result1 = [(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        
        result1 = [tupToDict(tup) for tup in result1]
        result2 = equipSubsets(fans)
        self.assertEqual(result1,result2)
    
    def test_33_real(self):
        fans = [3,3]
        result1 = [(0,1),(1,0),(1,1),(1,2)]
        
        result2 = equipSubsets(fans, real=True)
        result1 = [tupToDict(tup) for tup in result1]
        self.assertEqual(result1, result2)
    
    def test_222_2subsets(self):
        fans = [2,2,2]
        result1 = [(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0)]
        result2 = equipSubsets(fans, num_equip=2)
        result1 = [tupToDict(tup) for tup in result1]
        self.assertEqual(result1, result2)


class Test_foil(unittest.TestCase):
    """
    Test the foil functions
    """
    
    def test_foil2args_square(self):
        """
        (x+y)(x+y)==x^2+y^2+2xy==>
        {(2,0):1, (1,1):2, (0,2):1}
        """
        arg1 = {(1,0):1, (0,1):1}
        arg2 = arg1
        result = {(2,0):1, (1,1):2, (0,2):1}
        self.assertEqual(_foil2args(arg1,arg2),result)
    
    def test_foil2args_mod_int(self):
        """
        (x+y)(x+y)==x^2+y^2+2xy==>
        {(2,0):1, (0,2):1}
        """
        arg1 = {(1,0):1, (0,1):1}
        arg2 = arg1
        result = {(2,0):1, (0,2):1}
        self.assertEqual(_foil2args(arg1,arg2,2),result)
    
    def test_foil2args_mod_tup_same(self):
        """
        (x+y)(x+y)==x^2+y^2+2xy==>
        {(2,0):1, (0,2):1}
        """
        arg1 = {(1,0):1, (0,1):1}
        arg2 = arg1
        result = {(2,0):1, (0,2):1}
        self.assertEqual(_foil2args(arg1,arg2,(2,2)),result)
    
    def test_foil2args_mod_tup(self):
        """
        (3x+y)(2x+3y)%(6x,12y)==6x^2+3y^2+11xy==3y^2+5xy>
        {(1,1):5, (0,2):3}
        """
        arg1 = {(1,0):3, (0,1):1}
        arg2 = {(1,0):2, (0,1):3}
        result = {(0,2):3, (1,1):5}
        self.assertEqual(_foil2args(arg1,arg2,(6,12)),result)
    
    def test_foil(self):
        """
        (x+y)^3 == x^3 + 3xy^2 + 3x^2y + y^3
        """
        args = [{(1,0):1, (0,1):1}]*3
        res = {(3,0):1, (2,1):3, (1,2):3, (0,3):1}
        
        self.assertEqual(foil(args),res)
    
    def test_2vars_1s(self):
        """
        (x+y)(x+y) = x^2 + 2xy + y^2
        """
        sum1 = tupToDict((1,1))
        sum2 = tupToDict((1,1))
        
        result = {(2,0):1, (1,1):2, (0,2):1}
        
        self.assertEqual(result, _foil2args(sum1,sum2, None))
    
    def test_3vars_1s(self):
        """
        (x+y+z)(x+y+z) = x^2 + y^2 + z^2 + 2xy + 2xz + 2yz
        """
        sum1 = (1,1,1)
        sum2 = (1,1,1)
        
        result = {(2,0,0):1, (1,1,0):2, (1,0,1):2, (0,1,1):2, (0,0,2):1, (0,2,0):1}
        
        self.assertEqual(result, _foil2args(tupToDict(sum1),tupToDict(sum2), None))
    
    def test_2vars(self):
        """
        (x+2y)(3x-4y) = 3x^2 + 2xy - 8y^2
        """
        sum1 = tupToDict((1,2))
        sum2 = tupToDict((3,-4))
        
        result = {(2,0):3, (1,1):2, (0,2):-8}
        
        self.assertEqual(result, _foil2args(sum1,sum2, None))
    
    def test_dict(self):
        """
        (xy+x^2)(x+y) = 2x^2y + x^3 + xy^2
        """
        
        sum1 = {(1,1):1, (2,0):1}
        sum2 = tupToDict((1,1))
        
        result = {(2,1):2, (3,0):1, (1,2):1}
        
        self.assertEqual(result, _foil2args(sum1,sum2, None))
