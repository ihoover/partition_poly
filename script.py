from poly import *

# 4 3-fans
print "======= Four 3-fans ======="

p1 = Poly([3,3,3,3],2)
print "* Any 2 of 4:" + str(p1.minD)

p1 = Poly([3,3,3,3],3)
print "* Any 3 of 4:" + str(p1.minD)


# 4 5-fans
print "======= Four 5-fans ======="

p1 = Poly([5,5,5,5],2)
print "* Any 2 of 4:" + str(p1.minD)

p1 = Poly([5,5,5,5],3)
print "* Any 3 of 4:" + str(p1.minD)

# 5 3-fans
#print "======= Five 3-fans ======="

#p1 = Poly([3,3,3,3,3],2)
#print "* Any 2 of 5:" + str(p1.minD)

#p1 = Poly([3,3,3,3,3],3)
#print "* Any 3 of 5:" + str(p1.minD)

#p1 = Poly([3,3,3,3,3],4)
#print "* Any 4 of 5:" + str(p1.minD)
