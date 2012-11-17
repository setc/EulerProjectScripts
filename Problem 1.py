#-------------------------------------------------------------------------------
# Name:        Project Euler: Problem 1
# Purpose:     Find the sum of all the multiples of 3 or 5 below 1000.
#
# Author:      SebastiÃ¡n Torrente
#
# Comment:     Easy problem. Nothing out of the ordinary.
# Comment 2:   List comprenhesion is a thing of beauty.
#-------------------------------------------------------------------------------

def sumDiv(div1,div2,upto):
    """Calculate the sum of all the numbers below upto that can be divided by
    div1 or div2"""
    sum = 0
    divlist =  [x for x in range(upto) if (x % div1 == 0 or x % div2 == 0)]
    for num in divlist: sum += num
    return sum

if __name__ == '__main__':
    print (sumDiv(3, 5, 1000))
