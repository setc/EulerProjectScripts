#-------------------------------------------------------------------------------
# Name:        Problem 9
# Purpose:     There exists exactly one Pythagorean triplet for which
#              a + b + c = 1000. Find the product abc.
#
# Author:      Sebastián Torrente
#
# Created:     11/11/2012
# Comment:
#-------------------------------------------------------------------------------

def pythagTrip(sum):
    """Returns a Pythagorean triplet whith the condition a + b + c = 1000"""
    #We'll use the Euclide's Formula:
    trip = [1, 2, 3] # a, b, c
    for i in range(sum):
        m = i+1
        for n in range(m):
            trip = [m**2 - n**2, 2*m*n, m**2 + n**2]
            if trip[0] + trip[1] + trip[2] == sum: return trip


if __name__ == '__main__':
    triplet = pythagTrip(1000)
    abc = triplet[0] * triplet [1] * triplet[2]
    print(abc)
