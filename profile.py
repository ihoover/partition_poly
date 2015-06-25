import cProfile
from poly import Poly

cProfile.run("p=Poly([3,3,3,3,3],3); print p.minD")
