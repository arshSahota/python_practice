#normal list

# nums = [x*x for x in range(5)]

# print(nums)

#generator version

# nums = (x*x for x in range(5))
# print(nums)

#it does not store all values, it generates them when needed

#How to extract values
# for n in nums:
#     print(n)

#key idea
#lists = stores everything
# Generator = produces on demand

#yield ==> core of generators

#example

# def my_gen():
#     yield 1
#     yield 2
#     yield 3

#use it
# g = my_gen()

# for x in g:
#     print(x)

#difference between return vs yield
# def f():
#     return [1,2,3]
#returns everything at once

# def f():
#     yield 1
#     yield 2
#     yield 3

#gives values one by one

#normal way

# def get_squares(nums):
#     result = []

#     for num in nums:
#         result.append(num*num)
#     return result

#generator version
# def get_squares(nums):
#     for n in nums:
#         yield n*n

# for x in get_squares([1,2,3]):
#     print(x)

#why do we use generators:
# - memory efficiency
# - used for large data
# - used in real systems

#generators can be paused or resumed

def test():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("End")

g = test()
print(next(g))
print(next(g))

#it remembers where it left off