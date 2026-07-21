#what is error handling
# Errors happens when the program crashes
#print(10/0)
#crashes -> ZeroDivisionError

#error handling lets your program crash and handle the program safely

#basic structure
# try:
#     pass
#     #risky code
# except:
#     pass
#     #what to do if error happens

# try:
#     x = 10/0
# except:
#     print("Something went wrong")

#something went wrong

#catch specific errors
#better practice
# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("Cannot divide by 0")


#multiple exceptions
# try:
#     x = int("hello")
# except ValueError:
#     print("Invalid number")
# except TypeError:
#     print("Type Issue")

#else and finally

# try:
#     x = 10/2
# except ZeroDivisionError:
#     print("Error")
# else:
#     print("Success: ", x)
# finally:
#     print("Always runs")

# try: 
#     x = int("abc")
# except ValueError as e:
#     print("Error: ", e)

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     return age

# try:
#     print(check_age(-3))
# except ValueError as e:
#     print("Error:", e)