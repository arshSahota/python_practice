#list comprehension

# squares = [x*x for x in range(5)]

# print(squares)

#dictionary comprehension

# squares = {x: x*x for x in range(5)}

# print(squares)

#set comprehensions

# unique = {x for x in [1, 2, 2, 3, 3, 4]}
# print(unique)

#exercise

squares = [x*x for x in range(1,11) if x%2 == 0]
print(squares)