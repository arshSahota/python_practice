# You are given a list of HVAC device readings. Each device should operate between 18°C and 26°C.

# Write a function that:

# Identifies devices that are out of range.
# Returns a list of alarm messages.
# Counts the total number of alarms.

readings = {
    "AHU-01": 22.5,
    "VAV-101": 17.2,
    "VAV-102": 24.8,
    "RTU-01": 28.1,
    "FCU-03": 19.5
}

def check_hvac_alarms(readings):
    valid = []
    invalid = []
    count = 0
    for device, temp in readings.items():
        count+=1
        if 15 <= temp < 18:
            invalid.append(f"ALARM: {device} temperature too low ({temp}) and the severity is WARNING")
        elif temp < 15:
            invalid.append(f"ALARM: {device} temperature too low ({temp}) and the severity is CRITICAL")
        elif 26 < temp <= 30:
            invalid.append(f"ALARM: {device} temperature too high ({temp}) and the severity is WARNING")
        elif temp > 30:
            invalid.append(f"ALARM {device} temperature too high ({temp}) and the severity is CRITICAL")
        else:
            valid.append(device)

    alarm_percentage = (len(invalid)/count)*100

    return{
        "Invalid": invalid,
        "Total Devices": count,
        "Alarms": len(invalid),
        "Alarm Rate": f"{alarm_percentage}%"
    }


print(check_hvac_alarms(readings))