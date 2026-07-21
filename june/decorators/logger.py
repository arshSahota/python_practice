
def logger(func):
    def inner(*args, **kwargs):
        print("Calling function")
        func(*args, **kwargs)
        print("Function finished")
    return inner

@logger
def add(a, b):
    print(a+b)

add(2,3)