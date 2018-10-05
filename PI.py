
from math import sin 
from math import radians
from time import sleep


if __name__ == "__main__":
    print "The Radius is fixed in 1"
    print "the variable n is proption to calculate pi "
    n =  input("N = ") 
    r =  input("R =")
   
    x = 2*r*sin(radians(180.0 / float(n)))
    pi = (n*x)/(2*r)
    print "pi = %f" %(pi)
    print "the circleference = %f" %(pi * 2 * r)
    
    sleep(5)
    
    n = 1 
    r = 1 
   
    file = open('PI.txt', 'w')

    while True:
        x = 2 * r *sin(radians(180.0 / float(n)))
        pi = (n*x)/(2*r)
        file.write(str(pi)+"\n") 
        n += 1 
        print "try [{}] : {}".format(n , pi)
    #    sleep(0.000001)

    file.close()
        
   
    
