controllers = [
    {
        "controller": "CTRL-101",
        "cpu": 45,
        "memory": 60,
        "status": "HEALTHY",
        "services": ["HVAC", "ALARMS"]
    },
    {
        "controller": "CTRL-102",
        "cpu": 95,
        "memory": 72,
        "status": "HEALTHY",
        "services": ["LIGHTING"]
    },
    {
        "controller": "CTRL-103",
        "cpu": 35,
        "memory": 91,
        "status": "CRITICAL",
        "services": ["SECURITY", "ALARMS"]
    },
    {
        "controller": "CTRL-104",
        "cpu": 88,
        "memory": 89,
        "status": "WARNING",
        "services": ["HVAC"]
    }
]

def analyse_controllers(controllers):

    valid_controllers = set()
    invalid_controllers = {}
    critical_controllers = set()
    services_found = set()

    for reading in controllers:
        services_found.update(reading["services"])

        cpu = reading["cpu"]
        memory = reading["memory"]
        #determine expected status

        if cpu > 90 or memory > 90:
            expected_status = "CRITICAL"
        elif ( 80 <= cpu <= 90 or 80 <= memory <= 90):
            expected_status = "WARNING"
        else:
            expected_status = "HEALTHY"

        if expected_status == "CRITICAL":
            critical_controllers.add(reading["controller"])
        
        if expected_status == reading["status"]:
            valid_controllers.add(reading["controller"])
        else: 
            invalid_controllers[reading["controller"]] = (f"Expected {expected_status}, but got {reading['status']}")

    return {
        "valid_controllers": valid_controllers,
        "invalid_controllers": invalid_controllers,
        "critical_controllers": critical_controllers,
        "services_found": services_found
    }

print(analyse_controllers(controllers))