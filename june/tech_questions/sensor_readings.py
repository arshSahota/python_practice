sensor_data = [
    {
        "sensor_id": "S001",
        "temperature": 25,
        "humidity": 45,
        "battery": 90
    },
    {
        "sensor_id": "S002",
        "temperature": -5,
        "humidity": 50,
        "battery": 80
    },
    {
        "sensor_id": "S003",
        "temperature": 27,
        "humidity": None,
        "battery": 75
    },
    {
        "sensor_id": "S004",
        "temperature": 150,
        "humidity": 30,
        "battery": 120
    },
    {
        "sensor_id": "S005",
        "temperature": 20,
        "humidity": 60,
        "battery": 0
    }
]

def validate_sensor_data(sensor_data):

    valid_sensors = set()
    invalid_sensors = {}
    low_battery_sensors = set()
    summary = {}

    for data in sensor_data:

        id = data["sensor_id"]
        temp = data["temperature"]
        humidity = data["humidity"]
        battery = data["battery"]

        if battery <= 20:
            low_battery_sensors.add(id)

        if 0 <= temp <= 100 and humidity is not None and 0 <= humidity <= 100 and 1 <= battery <= 100:
            valid_sensors.add(id)
            summary["valid_count"] = summary.get("valid_count", 0) + 1

        if not 0 <= temp <= 100:
            invalid_sensors.setdefault(id, []).append("Temperature is out of range")
            summary["invalid_count"] = summary.get("invalid_count", 0) + 1
        elif humidity is None:
            invalid_sensors.setdefault(id, []).append("Humidity can't be None")
            summary["invalid_count"] = summary.get("invalid_count", 0) + 1
        elif not (0 <= humidity <= 100):
            invalid_sensors.setdefault(id, []).append("Humidity out of range")
            invalid_sensors[id] = summary.get("invalid_count", 0) + 1
        else:
            invalid_sensors.setdefault(id, []).append("Battery out of range")
            summary["invalid_count"] = summary.get("invalid_count", 0) + 1

        summary["total_sensors"] = summary.get("total_sensors", 0)+1


    return {
        "valid_sensors": valid_sensors,
        "invalid_sensors": invalid_sensors,
        "low_battery_sensors": low_battery_sensors,
        "summary": summary
    }

print(validate_sensor_data(sensor_data))