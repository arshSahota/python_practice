import time

def timer(func):
    def inner(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        res = time_end - time_start
        print("Time taken: ", res)
        return result
    return inner

@timer
def slow_function():
    for i  in range(100000):
        pass

slow_function()
