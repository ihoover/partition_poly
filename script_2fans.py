from poly import *

for fan_type in [2]:
    for num_fans in [2,3,4,5,6,7,8]:
        print "\n======= "+str(num_fans)+" "+str(fan_type)+"-fans ======="

        for k in range(2, num_fans+1):
            
            fans = [fan_type]*num_fans
            p1 = Poly(fans,k)
            if k < num_fans:
                print "\t* Any "+str(k)+" of "+str(num_fans)+":\t" + str(p1.minD)
            else:
                print "\t* All of "+str(num_fans)+":\t" + str(p1.minD)
