devices = [
    "AHU-01",
    "AHU-02",
    "VAV-01",
    "AHU-01",
    "VAV-01"
]

def find_duplicates(devices):
    seen = set()
    dupes = {}

    for device in devices:
        if device in seen:
            dupes[device] = dupes.get(device, 1)+1
        seen.add(device)

    return dupes

print(find_duplicates(devices))