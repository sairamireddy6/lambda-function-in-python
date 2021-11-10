from functools import  *

"""
def add_all(a,b):
    :return a+b


"""




is_even = lambda is_even: is_even % 2 == 0

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(is_even,nums))

doubles = list(map(lambda update : update + update,evens))

sum = reduce(lambda a,b : a + b ,doubles)

print("sum",sum)
print("even",evens)
print("doubles",doubles)
