
import math

def prime_gen(number):

    for p in range(2,int(number)+1):
        for i in range(2,p):
            if p%i == 0:
                break
        else:
            print (p)

    print ("Done")

print prime_gen(200)
