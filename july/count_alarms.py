# alarms = [
#     {"building": "Surrey", "status": "Open"},
#     {"building": "Surrey", "status": "Closed"},
#     {"building": "Burnaby", "status": "Open"},
#     {"building": "Surrey", "status": "Open"},
#     {"building": "Burnaby", "status": "Open"},
# ]

# def count_open_alarms(alarms):
#     alarms_per_building = {}

#     for alarm in alarms:
#         building = alarm["building"]
#         status = alarm["status"]

#         if status == "Open":
#             alarms_per_building[building] = alarms_per_building.get(building, 0) + 1

#     return alarms_per_building

# print(count_open_alarms(alarms))


alarms = [
    {"id": 1, "severity": "High"},
    {"id": 2, "severity": "Low"},
    {"id": 3, "severity": "Critical"},
    {"id": 4, "severity": "High"},
]

def most_common_severity(alarms):
    alm_count = {}

    for alarm in alarms:
        severity = alarm["severity"]
        alm_count[severity] = alm_count.get(severity, 0) + 1


    result = max(alm_count.items(), key=lambda x:x[1])

    return result

print(most_common_severity(alarms))