#from itertools import product
#from collections import Counter
from copy import copy

def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def count0s(tup):
    return sum(x==0 for x in tup)

# :'( python 2.4 was a sad place
def _all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def gcd_2(m,n):
	if n==0:
		return m
	r = m%n
	return(abs(gcd(n,r)))

def gcd(*args):
    return reduce(gcd_2, args)

def tupToDict(tup):
    """
    (a1,a2,a3,...,an) -->
    {(1,0,0,...,0):a1, (0,1,0,...,0):a2, ... ,(0,0,...,1):an}
    """
    
    def basis(i):
        base = [0]*len(tup)
        base[i] = 1
        return tuple(base)
    
    return {basis(i):tup[i] for i in range(len(tup))}


def allSwaps(n_vars):
    """
    returns all the dicts representing the polynomial
    (xi-xj) for all i<j and i,j<n_vars
    """
    
    dicts = []
    for i in range(n_vars):
        for j in range(i+1,n_vars):
            term = [0]*n_vars
            term[i] = 1
            term[j] = -1
            dicts.append(tupToDict(term))
    
    return dicts

def missingPerms(nVars, modP):
	"""
	Which permutations die?
	"""
	
	p = EquipPoly([modP]*nVars,2)
	actualTerms = [tuple((x-modP+1)/(modP-1) for x in key) for key in sorted(p.terms.keys())]
	
	allTerms = foil(allSwaps(nVars)*(modP-1))
	
	diff = sorted(list(set(allTerms) - set(actualTerms)))
	return diff

def equipSubsets(fans, num_equip=None, real=False):
    """
    Returns which Fourier coefficients must die.
    
    fans: iterable of fan numbers e.g. [2,2,3,4]
    num_equip: int that tells which subsets equipartition.  None = all, sorry :/
    real: bool true => real measure, false => complex measure
    """
    
    if num_equip is None:
        num_equip = len(fans)
    
    def inv(tup):
        """
        inverse a tuple representing a sum (for use with real mearsures)
        """
        return tuple(-tup[i]%fans[i] for i in range(len(fans)))
        
    coeffs = [tup for tup in product(*(range(x) for x in fans)) if count0s(tup) >= len(fans) - num_equip and sum(tup)>0]
    
    # purge duplicates if real
    if real:
        for i in reversed(xrange(int(len(coeffs)))):
            tup = coeffs[i]
            if inv(tup) != tup and inv(tup) in coeffs:
                coeffs.pop(i)
    
    # turn tuples into dictionaries representing polynomials in sum-of-products form
    return [tupToDict(tup) for tup in coeffs]

def _foil2args(sum1, sum2, mod_tup=None):
    """
    sum1: tuple or dict
    sum2: tuple
    mod: tuple describing the modding done on each component
    """
    result = {}
    allSame = False
    if mod_tup is not None:
        if type(mod_tup) == int:
            modc = mod_tup
            allSame = True

    for key1 in sum1:
        if sum1[key1] == 0:
            continue

        for key2 in sum2:
            # update the key with the new power
            val = sum1[key1]*sum2[key2]
            
            # the actual multiplying of the terms is adding the exponents
            new_key = tuple(key1[i]+key2[i] for i in range(len(key1)))
            if mod_tup is not None:
                if not allSame:
                    modc = mod_const(new_key, mod_tup)
                val %= modc
            
            if val == 0:
                continue
            
            if new_key in result:
                if mod_tup:
                    result[new_key] = (val + result[new_key]) % modc
                else:
                    result[new_key] += val
            else:
                result[new_key] = val
    removeZeros(result)
    return result


def removeZeros(terms):
    """
    Remove terms that are equal to zero
    """
    
    zero_keys = []
    for k in terms:
        if terms[k]==0:
            zero_keys.append(k)
        
    for k in zero_keys:
        terms.pop(k)


def mod_const(key, mod_tup):
    """
    the constant to reduce this power tuple
    """
    
    moduli = []
    for i in range(len(mod_tup)):
        if key[i] != 0:
            moduli.append(mod_tup[i])
    
    return gcd(*moduli)


def foil(terms, mod=None):
    """
    iterable of terms
    """
    return reduce(lambda x,y: _foil2args(x,y,mod), terms)


class Poly(object):
    """
    Class representing polynomial.  Initialized with dictionary representing the polynomial in sumOfProds form
    """
    
    def __init__(self, terms):
        
        self.terms = terms
    
    def __add__(self, other):
        """
        produce new polynomial
        """
        
        new_terms = copy(self.terms)
        
        for key in other.terms:
            if key in new_terms:
                new_terms[key] += other.terms[key]
            else:
                new_terms[key] = other.terms[key]
        removeZeros(new_terms)
        return Poly(new_terms)
    
    def __sub__(self, other):
        """
        produce new polynomial
        """
        
        new_terms = copy(self.terms)
        
        for key in other.terms:
            if key in new_terms:
                new_terms[key] -= other.terms[key]
            else:
                new_terms[key] = -other.terms[key]
        
        removeZeros(new_terms)
        return Poly(new_terms)

    def __mul__(self, other):
        """
        produce new polynomial
        """
        
        new_terms = foil([self.terms, other.terms])
        return Poly(new_terms)


class EquipPoly(Poly):
    """
    Class represents a polynomial for an equipartitioning problem
    """
    def __init__(self, fans, num_equip=None, real=False):
        """
        fans: iterable of fan numbers e.g. [2,2,3,4]
        num_equip: int that tells which subsets equipartition.  None = all, sorry :/
        real: bool true => real measure, false => complex measure
        """
        
        if num_equip is None:   
            num_equip = len(fans)
        
        self.fans = fans
        self.real = real
        self.num_equip = num_equip
        self.prodOfSums = equipSubsets(fans, num_equip, real)
        
        # if all fans are of equal size, mod constant is simple
        self.allSame = _all(fan == self.fans[0] for fan in self.fans)
        
        self.sumOfProds = foil(self.prodOfSums, fans)
        self.terms = self.sumOfProds
        try:
            self.minD = min(max(k) for k in self.sumOfProds)
        except:
            self.minD = None


def minD(poly):
    """
    returns the lowest dimension that leaves at least one term non-zero
    """

    min_max = -1
    for term in poly.split('+'):
        try:
            max_pow = max([int(x.split('^')[1]) for x in term.split(' ') if  '^' in x])
        except:
            print term
        if (max_pow < min_max) or (min_max < 0):
            min_max = max_pow

    return min_max
