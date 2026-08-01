temps = [21, 22, 25, 41, 20, 18, 43]

def generate_alarm(temps):
    result = []

    for temp in temps:
        if temp > 40:
            alarm = {}
            alarm["temperature"] = temp
            alarm["status"] = "ALARM"

            result.append(alarm)

    return result   

print(generate_alarm(temps))