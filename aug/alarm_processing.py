events = [
    {"device": "AHU-01", "temp": 22},
    {"device": "AHU-02", "temp": 41},
    {"device": "AHU-03", "temp": 18},
    {"device": "AHU-04", "temp": 45}
]

def check_events(events):
    return [
        {
            "device": event["device"],
            "alarm": "HIGH_TEMP"
        }
        for event in events
        if event["temp"] > 40
    ]

print(check_events(events))