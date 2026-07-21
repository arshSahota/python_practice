#filter ==> keeps the items that match a condition

#example:
# nums = [1,2,3,4]
# result = []

# for n in nums:
#     if n % 2 == 0:
#         result.append(n)

# print(result)

#with filter
nums = [1,2,3,4]
evens = list(filter(lambda x: x%2==0, nums))
print(evens)

#rule ==> filter(condition, list)

#combine map and filter
#example

nums = [1,2,4,5]

result = list(map(lambda x: x*x, filter(lambda x: x%2 ==0, nums)))

print(result)
