## A Narcissistic Number
## Please read the details of the problem in the link below:
## https://www.codewars.com/kata/5287e858c6b5a9678200083c/python
## (c) Miradiz Rakhmatov

def narcissistic(num):
    power = len(str(num))
    result = 0
    for i in str(num):
        result += (int(i))**power
    return result == num

