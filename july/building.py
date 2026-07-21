rooms = [
    {
        "room": "A101",
        "capacity": 20,
        "occupancy": 15
    },
    {
        "room": "A102",
        "capacity": 10,
        "occupancy": 12
    },
    {
        "room": "A103",
        "capacity": 50,
        "occupancy": 50
    },
    {
        "room": "A104",
        "capacity": 30,
        "occupancy": -2
    }
]

def validate_rooms(rooms):

    valid_rooms = []
    invalid_rooms = {}

    for item in rooms:
        number = item["room"]
        capacity = item["capacity"]
        occupancy = item["occupancy"]

        if 0<= occupancy <= capacity:
            valid_rooms.append(number)

        if occupancy < 0:
            invalid_rooms[number] = "Negative occupancy"

        if occupancy > capacity:
            invalid_rooms[number] = "Occupancy exceeds capacity"

    return {
        "valid_rooms": valid_rooms,
        "invalid_rooms": invalid_rooms
    }
        

print(validate_rooms(rooms))

#i would test boundary values like
#the occupancy can't be less than 0
#capacity and occupany limits align or not
#occupancy can be more than capacity
