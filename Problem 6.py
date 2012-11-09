#-------------------------------------------------------------------------------
# Name:        Problem 6
# Purpose:     Find the difference between the sum of the squares of the first
#              one hundred natural numbers and the square of the sum.
#
# Author:      Sebastián Torrente
#
# Created:     09/11/2012
#-------------------------------------------------------------------------------

def sumOfSquares(n):
    """Sum of the squares of the first n natural numbers."""
    sum = 0
    for i in range(n): sum += (i+1) ** 2
    return sum

def squareOfSum(n):
    """Square of the sum of the first n natural numbers."""
    sum = 0
    for i in range(n): sum += (i+1)
    return sum ** 2

def difSquares(n):
    """Difference between the sum of the squares of the first n natural numbers
    and the square of the sum."""
    return abs(squareOfSum(n)-sumOfSquares(n))

if __name__ == '__main__':
    print(difSquares(100))
