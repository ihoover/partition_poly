from poly import *

for fan_type in [5]:
    for num_fans in [2,3,4]:
        print "\n======= "+str(num_fans)+" "+str(fan_type)+"-fans ======="
        for real in [True, False]:
            if real:
                print "Real Measure:"
            else:
                print "Complex Measure:"
                
            for k in range(2, num_fans+1):
                
                fans = [fan_type]*num_fans
                p1 = Poly(fans,k,real)
                if k < num_fans:
                    print "\t* Any "+str(k)+" of "+str(num_fans)+":\t" + str(p1.minD)
                else:
                    print "\t* All of "+str(num_fans)+":\t" + str(p1.minD)
            
