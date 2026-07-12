sensors = [
    {"room": "A", "temperature": 25},
    {"room": "B", "temperature": 35},
    {"room": "C", "temperature": 17},
    {"room": "D", "temperature": 28}
]

def analyse_sensors(sensors):
    check_valid = {
        "VALID": {},
        "HIGH_TEMP": {},
        "LOW_TEMP": {}
    }

    for sensor in sensors:
        if 18 <= sensor["temperature"] <= 30:
            check_valid["VALID"][sensor["room"]] = sensor["temperature"]
        elif sensor["temperature"] > 30:
            check_valid["HIGH_TEMP"][sensor["room"]] = sensor["temperature"]
        else:
            check_valid["LOW_TEMP"][sensor["room"]] = sensor["temperature"]

    return check_valid

print(analyse_sensors(sensors))