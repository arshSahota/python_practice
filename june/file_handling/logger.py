def log_message(message):
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")
                
def log_function(func):
    def inner(*args, **kwargs):
        log_message(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        log_message(f"Function {func.__name__} Ended")
        return result
    return inner

@log_function
def add(a, b):
    return a+b

print(add(2,3))