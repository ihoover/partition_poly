from itertools import product
from collections import Counter

def gcd_2(m,n):
	if n==0:
		return m
	r = m%n
	return(abs(gcd(n,r)))

def gcd(*args):
    return reduce(gcd_2, args)


class Poly(object):
    """
    Class represents a polynomial for an equipartitioning problem
    """
    def __init__(self, fans, num_equip=None, real=True):
        """
        fans: iterable of fan numbers e.g. [2,2,3,4]
        num_equip: int that tells which subsets equipartition.  None = all, sorry :/
        real: bool true => real measure, false => complex measure
        """
        
        if num_equip is None:   
            num_equip = len(fans)
        
        self.fans = fans
        self.num_equip = num_equip
        self.prodOfSums = [tup for tup in product(*(range(x) for x in fans)) if Counter(tup)[0] >= len(fans) - num_equip and sum(tup)>0]
        
        # now, distribute...
        
        #for 

    def _foil_2args(self, sum1, sum2, mod=True):
        """
        sum1: tuple or dict
        sum2: tuple
        mod: bool
        """
        result = {}
        if type(sum1) is tuple:
            for i in range(len(sum1)):
                for j in range(len(sum2)):
                    val = sum1[i]*sum2[j]
                    if val == 0:
                        continue
                    
                    key = [0]*len(sum1)
                    key[i] += 1
                    key[j] += 1
                    key = tuple(key)
                    
                    
                    if key in result:
                        result[key] += val
                    else:
                        result[key] = val
        # sum1 is dict
        else:
            for i in range(len(sum2)):
                for key in sum1:
                    # update the key with the new power
                    val = sum1[key]*sum2[i]
                    if val == 0:
                        continue
                    new_key = list(key)
                    new_key[i] += 1
                    new_key = tuple(new_key)
                    
                    if new_key in result:
                        result[new_key] += val
                    else:
                        result[new_key] = val
        return result

    def foil(self, terms, mod=True):
        """
        iterable of terms
        """
        
        return reduce(self._foil_2args, terms)

def printPoly(num_fans, q, min_zero = 0):
    """
    Assumed that all fans are regular q-fans
    """

    variables = ['y'+ str(i) for i in range(1,num_fans+1)]
    sums=[]
    for tup in product(xrange(q), repeat=num_fans):
        # don't include the zero term
        if sum(tup) == 0 or (Counter(tup)[0] < min_zero):
            continue

        sums.append('('+' + '.join(['*'.join(term) for term in zip((str(x) for x in tup),variables)])+')')
        

    print ''.join(sums)


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

if __name__ == '__main__':

    p = Poly([3,3,3])
    
    print foil((0,2,3),(2,3,4))

    
