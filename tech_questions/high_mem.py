data = [
    {"memory": 40},
    {"memory": 80},
    {"memory": 95}
]

def highest_memory(data):

    high = 0

    for reading in data:
        if reading["memory"] > high:
            high = reading["memory"]
    
    return high

print(highest_memory(data))