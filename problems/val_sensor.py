readings = [
    {"sensor": "Room1", "temperature": 22},
    {"sensor": "Room2", "temperature": 45},
    {"sensor": "Room3", "temperature": -5},
    {"sensor": "Room4", "temperature": 19},
    {"sensor": "Room5", "temperature": 60}
]

def validate_readings(readings):
    valid = []
    invalid = []
    invalid_entries = []

    for reading in readings:
        if "sensor" in reading and "temperature" not in reading:
            invalid_entries.append({"sensor": reading["sensor"], "reason": "MISSING TEMPERATURE"})

        if "sensor" not in reading and "temperature" in reading:
            invalid_entries.append({"sensor": "MISSING", "temperature": reading["temperature"] })

        if "sensor" in reading and "temperature" in reading:
            sensor = reading["sensor"]
            temp = reading["temperature"]

            if 0 <= temp <= 50:
                valid.append({"sensor": sensor, "temperature": temp})
            else:
                invalid.append({"sensor": sensor, "temperature": temp, "reason": "OUT_OF_RANGE"})

    return {
        "valid": valid,
        "invalid": invalid,
        "valid_count": len(valid),
        "invalid_count": len(invalid),
        "invalid_entries": invalid_entries
    }

print(validate_readings(readings))