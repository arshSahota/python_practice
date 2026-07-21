# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Hello", name, "you are", age, "years old")

# celcius = float(input("Enter temperature in Celcius: "))

# ftemp = (celcius * 9/5) + 32

# print("Temperature in Fahrenheit is: ", ftemp)

# sentence = input("Enter a sentence please: ")
# count = 0

# for char in sentence:
#     count+=1

# print("Count: ", count)

def reverse_string(sentence):
    return sentence[::-1]

sentence = "hello"

print(reverse_string(sentence))
