# alarms = [
#     "RTU-01",
#     "RTU-01",
#     "AHU-07",
#     "RTU-01",
#     "AHU-07"
# ]

# alarm_count = {}

# for alarm in alarms:

#     alarm_count[alarm] = alarm_count.get(alarm, 0) + 1

    
# print(alarm_count)

# problem 2
# alarms = [
#     {"severity": "HIGH"},
#     {"severity": "HIGH"},
#     {"severity": "LOW"},
#     {"severity": "CRITICAL"}
# ]

# severity_count = {}

# for alarm in alarms:
#     severity_count[alarm["severity"]] = severity_count.get(alarm["severity"], 0)+1

# print(severity_count)

#level 2 sets
devices = [
    "RTU-01",
    "AHU-07",
    "RTU-01",
    "VAV-12"
]

#I will return true if duplicate exists and false otherwise

check_dups = set()

for device in devices:
    if device in check_dups:
        print(True)
    check_dups.add(device)
