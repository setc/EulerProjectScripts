#-------------------------------------------------------------------------------
# Name:        Project Euler: Problem 1
# Purpose:     Find the sum of all the multiples of 3 or 5 below 1000.
#
# Author:      Sebastián Torrente
#
# Comment:     Easy problem. Nothing out of the ordinary.
#-------------------------------------------------------------------------------

def sumDiv(div1,div2,upto):
    """Calculate the sum of all the numbers below upto that can be divided by
    div1 or div2"""
    sum = 0
    for i in range(upto):
        if (i % div1 == 0 or i % div2 == 0): sum += i
    return sum

if __name__ == '__main__':
    print (sumDiv(3, 5, 1000))
