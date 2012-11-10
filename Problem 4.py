#-------------------------------------------------------------------------------
# Name:        Project Euler Problem 4
# Purpose:     Find the largest palindrome made from the product of two 3-digit
#              numbers.
#
# Author:      SebastiÃ¡n Torrente
#
# Created:     08/11/2012
# Comment:     Easier than it seems if you think in advance. Python makes the
#              construction of palindrome numbers a breeze.
#
# Notes:       -If we are looking for the greatest palindrome, is going to be a
#              six digits number.
#              -There are 899 palindromes with six digits: from 100001 to
#              999999
#              -888888 = 924 * 962 and 999 * 999 = 998001, so our number should
#              be between 889988 and 997799
#              -So I'll iterate from 997 to 889 (97) and dividing each
#              palindrome numbers iterating from 999 to 924 (75)
#-------------------------------------------------------------------------------

def palindrocreate(n):
    """Creates a palindrome number attaching n inverted to the end.
    Example: palindrocreate(123) = 123321"""
    part = str(n)
    return int(part+part[::-1])

construct = 997
while construct >= 889:

    pal, div1, div2 = palindrocreate(construct), 999, 1
#    print(pal)

    while div1 >= 924:
        if pal % div1 == 0:
            div2 = pal // div1
#            print (div2)
            if len(str(div2)) == 3: print (construct)
        div1 -= 1
    construct -= 1


#if __name__ == '__main__':
#    print (palindrocreate(123))

