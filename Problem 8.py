#-------------------------------------------------------------------------------
# Name:        Problem 8
# Purpose:     Find the greatest product of five consecutive digits in the
#              1000-digit number.
#
# Author:      Sebastián Torrente
#
# Created:     10/11/2012
# Comment:     I don't understand exactly what are asking me here. I guess is
#              'iterate the numbers and find the greatest value of the product
#              of five consecutive numbers.
#-------------------------------------------------------------------------------

def consecProdMax(inter, n):
    """Take a string of ONLY numbers inter and find the maximum product of n
    consecutive numbers inside it"""

    nums = []
    for char in inter: nums.append(int(char))
    sol = 0

    for i in range(len(nums) - n):
        prod = 1
        for j in range(n): prod *= nums[i + j]
        if prod > sol: sol = prod
    return sol

if __name__ == '__main__':
    test = '123456789874563578966542'
    print('Test Chain' = test)
    print('concecProdmax(test,5) = ',consecProdMax(test,5))
#Solution for the Problem 8. Need to solve the route error when I put only
#\Data\data8.txt
#    chain = open(r'C:\Python32\EulerProjectScripts\Data\data8.txt')
#    data = chain.read()

#    print (consecProdMax(data, 5))