## Moving Zeros To The End
## Please read the details of the problem in the link below:
## https://www.codewars.com/kata/52597aa56021e91c93000cb0
## (c) Miradiz Rakhmatov

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(0)
    return array