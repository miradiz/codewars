## Digital Root
## Please read the details of the problem in the link below:
## https://www.codewars.com/kata/541c8630095125aba6000c00
## (c) Miradiz Rakhmatov

def digital_root(number):
    num = [int(i) for i in str(number)]
    while len(str((sum(num)))) > 1:
        num = [int(i) for i in str(sum(num))]
    return sum(num)

