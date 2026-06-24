#what map does ==> applies to a all items in a list

#example
# nums = [1,2,3]

# squares = []

# for n in nums:
#     squares.append(n*n)

#with map
nums = [1,2,3]

squares = list(map(lambda x: x*x, nums))

print(squares)

#rule 
#map(function, list)


