## Your order
## Please read the details of the problem in the link below:
## https://www.codewars.com/kata/55c45be3b2079eccff00010f
## (c) Miradiz Rakhmatov

def order(string):
    if string != "":
        new = list()
        for i in range(10):
            for s in string.split():
                if str(i) in s:
                    new.append(s)
        return ' '.join(new)
    return ""

