devices = [
    {"name": "AHU-01", "status": "online", "alarms": 0},
    {"name": "AHU-02", "status": "offline", "alarms": 0},
    {"name": "VAV-01", "status": "online", "alarms": 3},
    {"name": "VAV-02", "status": "online", "alarms": 0},
]

def check_devices(devices):

    healthy = []
    unhealthy = []

    for device in devices:

        name = device["name"]
        status = device["status"]
        alarms = device["alarms"]

        reasons = []

        if status == "offline":
            reasons.append("OFFLINE")

        if alarms > 0:
            reasons.append("ACTIVE_ALARMS")

        if reasons: 
            unhealthy.append(
                {
                    "name": name,
                    "reason": reasons
                }
            )
        else:
            healthy.append({
                "name": name,
            })

    return {
        "healthy": healthy,
        "unhealthy": unhealthy
    }


print(check_devices(devices))