response = {
    "deviceId": 123,
    "name": "AHU-01",
    "status": "online",
    "temperature": 22.5
}

def validate_device(response):

    errors = []

    if "deviceId" not in response:
        errors.append("deviceId missing")

    elif not isinstance(response["deviceId"], int):
        errors.append("deviceId must be a number")


    if "name" not in response:
        errors.append("name missing")
    elif response["name"] == "":
        errors.append("name cannot be empty")

    if "status" not in response:
        errors.append("status missing")
    elif response["status"] not in ["online", "offline"]:
        errors.append("status must be online or offline")

    if "temperature" not in response:
        errors.append("temperature missing")
    elif not isinstance(response["temperature"], (int, float)):
        errors.append("temperature must be a number")

    if errors:
        return False, errors

    return True, []

print(validate_device(response))