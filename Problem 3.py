#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 3
# Purpose:     What is the largest prime factor of the number 600851475143 ?
#
# Author:      Sebastián Torrente
#
# Created:     08/11/2012
# Comment:     Surpisingly, it doesn't need as much optimization as I thought.
#              Should refactor in the future just in case, though.
#-------------------------------------------------------------------------------

def primeFactors(n):
    """Pretty simple function to find the prime factors of x"""

    if n % 2 == 0: factorlist = [2] #Let's take the even numbers out.
    else: factorlist = []

    count = 3

    while count <= n:
        if n % count == 0:
            n /= count
            factorlist.append(count)
        else:
            count += 2 #We are only iterating through the odd numbers.
    return factorlist

if __name__ == '__main__':
    print (max(primeFactors(600851475143)))
