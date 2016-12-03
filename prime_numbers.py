
import math

def prime_gen(number):
    prime_number_list=[]

    for p in range(2,int(number)+1):
        for i in range(2,p):
            if p%i == 0:
                break
        else:
            prime_number_list.append(p)
    print prime_check(prime_number_list)

def prime_check(number_list):
    stat_list=[]
    result={}
    size = len(number_list)

    for number in number_list:
        if number <= 1:
            stat_list.append("Not Prime")
        elif number % number+1 == 0:
            stat_list.append("Not Prime")
        else:
            stat_list.append("Prime")
    size=size-1
    while size > 0 :
        result={number_list[size],stat_list[size]}
        print result
        size -= 1

print prime_gen(200)
