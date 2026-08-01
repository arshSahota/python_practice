events = [
    {"type": "alarm", "id": 1},
    {"type": "alarm", "id": 2},
    {"type": "report", "id": 3},
]

grouped = {}

for event in events:
    if event["type"] not in grouped:
        grouped[event["type"]] = []

    grouped[event["type"]].append(event)

print(grouped)
    
