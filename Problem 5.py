#-------------------------------------------------------------------------------
# Name:        Problem 5
# Purpose:     What is the smallest positive number that is evenly divisible by
#              all of the numbers from 1 to 20?
#
# Author:      Sebastián Torrente
#
# Created:     09/11/2012
# Comments:    Let's analize first the properties of 2520 as the smallest number
#              that can be divided by each of the numbers from 1 to 10 without
#              any remainder.
#              * 2520 = 2**3 * 3**2 * 5 * 7
#              Ring any bell? It should, is the product of all the prime numbers
#              below 10 each one at the higher possible power without surpassing
#              10.
#              This give us the key to develop a generic solution for a number n:
#                  -Make a list of all the prime numbers under n
#                  -For each number find the highest exponential you can give it
#
#              The solution can be calculated by hand without problem:
#                  - 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
#              Let's see if we can make it via script too.
#-------------------------------------------------------------------------------



def smallEvenlyDiv(n):
    """Find the smallest positive number that is evenly divisible by all of the
    numbers from 1 to n"""
#    primList, listsol, prodsol = primes(n), [], 1
    primList, listsol, prodsol = [2,3,5,7,11,13,17,19], [], 1 #Add a primes(n) function later
    for number in primList:
        power = 1
        while number ** power <= n: power += 1
        listsol.append(number ** (power - 1))

    for number in listsol: prodsol *= number

    return prodsol

if __name__ == '__main__':
    print (smallEvenlyDiv(20))
