import unittest
from poly import Poly

class Testp_foil_2args(unittest.TestCase):
    """
    Tests for the p._foil_2args operation
    """
    
    def setUp(self):
        self.p = Poly([0])
    
    def test_2vars_1s(self):
        """
        (x+y)(x+y) = x^2 + 2xy + y^2
        """
        sum1 = (1,1)
        sum2 = (1,1)
        
        result = {(2,0):1, (1,1):2, (0,2):1}
        
        self.assertEqual(result, self.p._foil_2args(sum1,sum2, False))
    
    def test_3vars_1s(self):
        """
        (x+y+z)(x+y+z) = x^2 + y^2 + z^2 + 2xy + 2xz + 2yz
        """
        sum1 = (1,1,1)
        sum2 = (1,1,1)
        
        result = {(2,0,0):1, (1,1,0):2, (1,0,1):2, (0,1,1):2, (0,0,2):1, (0,2,0):1}
        
        self.assertEqual(result, self.p._foil_2args(sum1,sum2, False))
    
    def test_2vars(self):
        """
        (x+2y)(3x-4y) = 3x^2 + 2xy - 8y^2
        """
        sum1 = (1,2)
        sum2 = (3,-4)
        
        result = {(2,0):3, (1,1):2, (0,2):-8}
        
        self.assertEqual(result, self.p._foil_2args(sum1,sum2, False))
    
    def test_dict(self):
        """
        (xy+x^2)(x+y) = 2x^2y + x^3 + xy^2
        """
        
        sum1 = {(1,1):1, (2,0):1}
        sum2 = (1,1)
        
        result = {(2,1):2, (3,0):1, (1,2):1}
        
        self.assertEqual(result, self.p._foil_2args(sum1,sum2, False))
  
    def test_3terms(self):
        """
        (x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3
        """
        terms = [(1,1),(1,1),(1,1)]
        result = {(3,0):1, (2,1):3, (1,2):3, (0,3):1}
        
        self.assertEqual(self.p.foil(terms, False),result)
