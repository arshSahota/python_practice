def classify_temp(temp):
    if 18 <= temp <= 30:
        return "VALID"
    elif 30 < temp:
        return "HIGH_TEMP"
    else:
        return "LOW_TEMP"


# mini exerise2: 

# if the dev changes the function that way, then the boundary values are 
# not included and then the boundary value 30 is included in the HIGH TEMP vals

# 1. Which test fails
# Ans: The 18, 30 
# Ans2: 18 because its not included in the boundary values
# Ans 3: code bug

#mini exercise 4 function

def check_alarm(sensor):
    if sensor["temperature"] > 30:
        return True
    else:
        return False

