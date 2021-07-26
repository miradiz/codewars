## Create Phone Number
## Please read the details of the problem in the link below:
## https://www.codewars.com/kata/525f50e3b73515a6db000b83
## (c) Miradiz Rakhmatov

def create_phone_number(n):
    s = ''.join([str(i) for i in n])
    return"({}) {}-{}".format(s[:3], s[3:6], s[6:])