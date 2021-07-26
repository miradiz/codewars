## Count the number of Duplicates
## Please read the details of the problem in the link below:
## https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
## (c) Miradiz Rakhmatov

def duplicate_count(string):
    count = 0
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            count += 1
            string = string.replace(i, "")
    return count