def log_message(message):
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")
    
def logger(func):
    def inner(*args, **kwargs):
        log_message(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        log_message(f"Function {func.__name__} ended")
        return result
    return inner

@logger
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(f"[ ] {task}\n")

def view_tasks():
    count=1
    with open("tasks.txt", "r") as f:
        for line in f:
            print(f"{count}: {line.strip()}")
            count+=1
@logger
def mark_done(task_number):
    try: 
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No tasks found")
            log_message("Error: No Tasks Found")
            return
        if task_number < 1 or task_number > len(lines):
            print("Invalid task number")
            log_message("Error: Invalid task numbe")
            return
        
        with open("tasks.txt", "w") as f:
            count = 1
            for line in lines:
                if count == task_number:
                    task_name = line[4:].strip()
                    line = "[x] " + line[4:]
                f.write(line)
                count+=1
    except FileNotFoundError:
        print("No tasks file found")
        log_message("Error: File not found")
    except ValueError:
        print("Invalid input")

while True:
    task = input("Enter a task here: ")
    if task == "q":
        break
    add_task(task)

view_tasks()
num = int(input("Enter task number to mark done: "))
mark_done(num)
view_tasks()