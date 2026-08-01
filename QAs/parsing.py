data = [
    "Room1:22",
    "Room2:25",
    "Room3:19"
]
parsed_data = {}

for entry in data:
    parts = entry.split(":")

    parsed_data[parts[0]] = int(parts[1])


average = sum(parsed_data.values())/len(parsed_data.values())
print(average)


