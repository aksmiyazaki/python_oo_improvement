def square(num):
    return num ** 2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']

list(map(splicer, names))

def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

list(filter(check_even, mynums))

square = lambda num: num ** 2
square(4)

list(filter(lambda x: x % 2 == 0, mynums))
