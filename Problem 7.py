#-------------------------------------------------------------------------------
# Name:        Problem 7
# Purpose:     What is the 10001st prime number?
#
# Author:      Sebastián Torrente
#
# Created:     10/11/2012
# Comment:     This one has no mistery, but is going to be useful in the future
#-------------------------------------------------------------------------------

def isprime(x):
    """Find if x is prime counting from n onwards."""
    for divisor in range(2, int(x**0.5)+1):
        if x / divisor == int(x / divisor):
            return False
    return True

def isprime2(n):
    """A version more optimized for future uses."""
    n *= 1.0
    if n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3:
        return False
    for b in range(1,int((n**0.5+1)/6.0+1)):
        if n%(6*b-1)==0:
            return False
        if n %(6*b+1)==0:
           return False
    return True

def primelist(n):
    """Return a list with the first n prime numbers."""
    listprim=[2,3,5,7,11,13,17,19] #Let's put some of them to save a little bit
                                   #of brainpower.
    init = 23
    while len(listprim) < n:
        if isprime2(init) == True: listprim.append(init)
        init += 1

    return listprim

if __name__ == '__main__':
    print (primelist(10001)[-1])
#    print(isprime(23))