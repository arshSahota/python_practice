valid = {
    "temperature": 32,
    "alarm": True,
    "energy_usage": 1200
}

invalid = {
    "temperature": 32,
    "alarm": False,
    "energy_usage": 1200
}
# temperature > 30
# => alarm must be True
# temperature <= 30
# => alarm must be False
# energy_usage must never be negative

def validate_building_response(response):
    if response["energy_usage"] < 0:
        return False
    if response["temperature"] > 30:
        return response["alarm"] is True
    else:
        return response["alarm"] is False

print(validate_building_response(valid))
print(validate_building_response(invalid))

#etxra question answer
# if it returns false, I would try to specific about what caused the failure, whether its energy usage, temp or alarm status

# assert response["alarm"] is True, (
#     f"Expected alarm=True when temperature is "
#     f"{response['temperature']}"
# )