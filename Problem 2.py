#-------------------------------------------------------------------------------
# Name:        Euler project 2
# Purpose:     By considering the terms in the Fibonacci sequence whose values
#              do not exceed four million, find the sum of the even-valued terms
#
# Author:      SebastiÃ¡n Torrente
#
# Created:     07/11/2012
#-------------------------------------------------------------------------------

def fibonacci(n): #Do not use: too slow!!
    """Just a function that calculate the n term in the fibonacci series.
    Actually taken from:
    http://stackoverflow.com/questions/494594/
    how-to-write-the-fibonacci-sequence-in-python"""
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)

def fib(n): #Better, but still slow.
    """Fibonacci function from
    http://en.literateprograms.org/Fibonacci_numbers_(Python)
    Actually faster than the former, still not enough."""
    memo = {0:0, 1:1}
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def fibonacciSum(upto,divisor):
    """This function calculates the sum of the terms in a fibonacci series upto
    that can be divided by divisor."""
    sum = 0
    num = 1
    while fib(n) < upto:
        if fib(n) % divisor == 0:
            sum += sum + num
    num += 1
    return sum

#All code so far may be elegant, but is very inefficient. For each cycle of
#fibonacciSum we have to calculate the fibonacci number n two times! And we need
#all of them which are lower than 4,000,000.

#And that's the key. We need all of them, so let's use a list.

def fiblist(upto): #Fibonacci, the "GOTTA GO FAST!" version
    """Create a list Fibonacci's series elements with values below upto."""
    base = [0, 1]
    if (upto==0 or upto==1): return [0]

    while base[-1] < upto:
        next = base[-1] + base [-2]
        base.append(next)

    base.pop()
    return base

def fiblistSum(lst,div):
    sol=0
    for n in lst:
        if n % div == 0: sol += n
    return sol

if __name__ == '__main__':
    sol = fiblistSum(fiblist(4000000),2)
    print (sol)
