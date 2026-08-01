logs = [
    "INFO: Device Connected",
    "ERROR: BACnet timeout",
    "INFO: Dashboard Loaded",
    "ERROR: Database Unreachable",
    "WARNING: Memory High",
    "ERROR: BACnet timeout"
]

def check_errors(logs):
    error_counts = {}
    error_types = {}

    for msg in logs:
        parts = msg.split(": ")

        error_counts[parts[0]] = error_counts.get(parts[0], 0) + 1

        if parts[0] == "ERROR":
            error_types[parts[1]] = error_types.get(parts[1], 0) + 1

    return max(error_types, key=error_types.get)
    

print(check_errors(logs))