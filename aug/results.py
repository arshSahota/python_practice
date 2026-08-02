expected = {
    "temperature": 22,
    "humidity": 50,
    "occupied": True
}

actual = {
    "temperature": 22,
    "humidity": 47,
    "occupied": False
}

def find_differences(expected, actual):
    differences = {}

    for key in expected:
        if expected[key] != actual[key]:
            differences[key] = {
                "expected": expected[key],
                "actual": actual[key]
            }

    return differences

print(find_differences(expected, actual))
