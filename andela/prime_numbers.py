
import math

def prime_gen(number):
    if number < 0:
        print "Negative number, not allowed"

    while True:
        primetest = True
        for x in range(2, int(math.sqrt(number) + 1)):
            if number % x == 0:
                primetest = False
                break
        if primetest and number >1:
            print number
        number -= 1

print prime_gen(6)
