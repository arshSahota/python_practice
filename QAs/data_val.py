expected = {
    "temperature": 22,
    "humidity": 50,
    "alarm": False
}

actual = {
    "temperature": 22,
    "humidity": 55,
    "alarm": False
}

def validate_data(expected, actual):
    differences = {}

    if expected["temperature"] != actual["temperature"]:
        differences["temperature"] = {
            "expected": expected["temperature"],
            "actual": actual["temperature"]
        }

    if expected["humidity"] != actual["humidity"]:
        differences["humidity"] = {
            "expected": expected["humidity"],
            "actual": actual["humidity"]
        }

    if expected["alarm"] != actual["alarm"]:
        differences["alarm"] = {
            "expected": expected["alarm"],
            "actual": actual["alarm"]
        }

    return differences

print(validate_data(expected, actual))