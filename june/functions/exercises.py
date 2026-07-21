#exercise 1

# triple = lambda x: x*3
# print(triple(2))

#exercise 2
nums = [1,2,3,4]

doubles = list(map(lambda x: x*2, nums))
print(doubles)

#exercise 3
nums = [5, 10, 15, 20]

n = list(filter(lambda x: x>10, nums))
print(n)

#exercise #4
nums = [1,2,3,4,5,6]

# squares = list(map(lambda x: x*x, filter(lambda x: x>3, nums)))

# print(f"Squares of numbers greater than 3 {squares}")

n = [x*x for x in nums if x >3]
print(n)