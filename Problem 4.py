#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 4
# Purpose:     Find the largest palindrome made from the product of two 3-digit
#              numbers.
#
# Author:      Sebastián Torrente
#
# Created:     08/11/2012
# Comment:     Easier than it seems if you think in advance. Python makes the
#              construction of palindrome numbers a breeze.
#
# Notes:       -If we are looking for the greatest palindrome, is going to be a
#              six digits number.
#              -There are 899 palindromes with six digits: from 100001 to
#              999999
#-------------------------------------------------------------------------------

def palindrocreate(n):
    """Creates a palindrome number attaching n inverted to the end.
    Example: palindrocreate(123) = 123321"""
    part = str(n)
    return int(part+part[::-1])

construct = 995 #You don't need to begin at 999999 because 999*999=998001
while construct <= 100:
    pal = palindrocreate(construct)
    div1 = 999
    div2 = 0
    while div1 <= 100:
        if pal % div1 == 0:
            div2 = pal // div1
            if len(str(div2)) == 3: return construct
        div -= 1
    construct -= 1

print (construct)


#if __name__ == '__main__':
#    print (palindrocreate(123))

