
def is_prime(number):
    if number <0:
        print "Negative Numbers Not allowed"

    l=[]
    while number > 0:
        if number%2 == 1 and number%3 ==1 and number%5 == 1 and number%number == 0 :
            l.append(number)
            number = number-1
        else:
            number= number - 1
        number = number - 1

    return l

print is_prime(10)
