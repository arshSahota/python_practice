servers = [
    {"name": "Server1", "cpu": 45, "mem": 60},
    {"name": "Server2", "cpu": 85, "mem": 40},
    {"name": "Server3", "cpu": 55, "mem": 95},
    {"name": "Server4", "cpu": 30, "mem": 50},
]

cpu_threshold = 80
mem_threshold = 90

def validate_servers(servers, cpu_threshold, mem_threshold):
    valid = []
    invalid = []

    for server in servers:

        reading = {
            "name": server["name"],
            "cpu": server["cpu"],
            "mem": server["mem"]
        }

        if (
            server["cpu"] < cpu_threshold
            and server["mem"] < mem_threshold
        ):
            valid.append(reading)
        else:
            invalid.append(reading)

    return {
        "valid": valid,
        "invalid": invalid
    }

print(validate_servers(servers, cpu_threshold, mem_threshold))