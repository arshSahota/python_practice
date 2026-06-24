def count_up(n):
    for i in range(1,n+1):
        yield i
    
g = count_up(3)

for x in g:
    print(x)

#exercise #2
print("Exercise #2")
nums = [1,2,3,4]

def squares(nums):
    for num in nums:
        yield num*num

g = squares(nums)

for x in g:
    print(x)

print("Exercise #3")

def evens_only(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

g = evens_only(nums)

for x in g:
    print(x)
    print(f"Test: {x}")

#important ==> generators are used once only!