sensors = [
    {
        "room": "Server Room",
        "temperature": 35,
        "alarm": True,
        "equipment": ["UPS", "CoolingUnit"]
    },
    {
        "room": "Office 101",
        "temperature": 24,
        "alarm": False,
        "equipment": ["Thermostat"]
    },
    {
        "room": "Storage Room",
        "temperature": 15,
        "alarm": False,
        "equipment": ["Sensor"]
    },
    {
        "room": "Electrical Room",
        "temperature": 33,
        "alarm": False,
        "equipment": ["Generator", "UPS"]
    }
]

valid_rooms = set()
invalid_rooms = {}
equipment_found = set()

def analyse_sensors(sensors):
    for reading in sensors:
        for item in reading["equipment"]:
            equipment_found.add(item)
        if reading["temperature"] > 30 and reading["alarm"] is True:
            valid_rooms.add(reading["room"])
        elif reading["temperature"] <= 30 and reading["alarm"] is False:
            valid_rooms.add(reading["room"])
        elif reading["temperature"] <= 30 and reading ["alarm"] is True:
            invalid_rooms[reading["room"]] = "Temperature below 30 but alarm was on"
        else:
            invalid_rooms[reading["room"]] = "Temperature above 30 but alarm was off"
    return {
        "valid_rooms": valid_rooms,
        "invalid_rooms": invalid_rooms,
        "equipment_found": equipment_found
    }

print(analyse_sensors(sensors))