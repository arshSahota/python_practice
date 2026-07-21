schedules = [
    {
        "building": "North Tower",
        "start_hour": 8,
        "end_hour": 18,
        "enabled": True
    },
    {
        "building": "South Tower",
        "start_hour": 20,
        "end_hour": 18,
        "enabled": True
    },
    {
        "building": "East Tower",
        "start_hour": 7,
        "end_hour": 17,
        "enabled": False
    },
    {
        "building": "West Tower",
        "start_hour": 9,
        "end_hour": 21,
        "enabled": True
    }
]

def analyse_schedules(schedules):
    valid_buildings = set()
    invalid_buildings = {}
    disabled_buildings = set()

    for schedule in schedules:

        building = schedule["building"]
        start = schedule["start_hour"]
        end = schedule["end_hour"]
        status = schedule["enabled"]
        duration = end-start

        if status is False:
            disabled_buildings.add(building)

        elif start > end:
            invalid_buildings[building] = ("Start time must be earlier than end time")
        
        elif duration > 12:
            invalid_buildings[building] = ("Schedule exceeds 12 hours")

        else:
            valid_buildings.add(building)

    return{
        "valid_buildings": valid_buildings,
        "invalid_buildings": invalid_buildings,
        "disabled_buildings": disabled_buildings
    }

print(analyse_schedules(schedules))