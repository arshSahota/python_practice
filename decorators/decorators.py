# def greet():
#     print("Hello")

#wrapping it manually

# def wrapper(func):
#     def inner():
#         print("Before")
#         func()
#         print("After")
#     return inner

# greet = wrapper(greet)

# greet()

#cleaner usage
def wrapper(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

@wrapper
def greet():
    print("hello")

# @wrapper def greet() means ==> greet = wrapper(greet)
greet()

#important rule

# to handle any function
# def wrapper(func):
# def inner(*args, **kwargs):
#   print( "Before")
#   func()
#   print("After")
#return inner

# *args and *kwargs work for any function
