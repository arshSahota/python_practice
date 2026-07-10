# #problem 1
# devices = [
#     "RTU",
#     "AHU",
#     "RTU",
#     "VAV",
#     "RTU"
# ]

# device_count = {}

# for device in devices:
#     device_count[device] = device_count.get(device, 0) + 1

# print(device_count)

# #problem #2
# alarms = [
#     {"building": "Hospital"},
#     {"building": "School"},
#     {"building": "Hospital"},
#     {"building": "Mall"}
# ]

# alarms_by_building = {}

# for alarm in alarms:
#     alarms_by_building[alarm["building"]] = alarms_by_building.get(alarm["building"], 0) + 1

# print(alarms_by_building)

# #problem #3
# alarms = [
#     {"severity": "HIGH"},
#     {"severity": "LOW"},
#     {"severity": "HIGH"},
#     {"severity": "CRITICAL"},
#     {"severity": "HIGH"}
# ]

# severity_counts = {}

# for alarm in alarms:
#     severity_counts[alarm["severity"]] = severity_counts.get(alarm["severity"], 0) + 1

# max_key, max_value = max(severity_counts.items(), key = lambda item: item[1])

# print(max_key)

# //batch 2
# alarms = [
#     {"building": "Hospital"},
#     {"building": "School"},
#     {"building": "Hospital"},
#     {"building": "Mall"}
# ]

# unique_build = set()

# for alarm in alarms:
#     if alarm["building"] not in unique_build:
#         unique_build.add(alarm["building"])

# print(unique_build)

#problem b2
# unique = set()

# def duplicate_devices(list):
#     for item in list:
#         if item in unique:
#             return True
#         unique.add(item)

# print(duplicate_devices([
#     "RTU",
#     "AHU",
#     "RTU"
# ]))

#problem 3

# unique = set()
# dupes = set()

# def return_all_dupes(list):
#     for item in list:
#         if item in unique:
#             dupes.add(item)
#         unique.add(item)
#     return dupes

# print(return_all_dupes([
#     "RTU",
#     "AHU",
#     "RTU",
#     "VAV",
#     "AHU"
# ]))

#Batch 3 Grouping
# alarms = [
#     {"building": "Hospital", "device": "RTU"},
#     {"building": "School", "device": "AHU"},
#     {"building": "Hospital", "device": "VAV"}
# ]

# group_by_building = {}

# for alarm in alarms:
#         group_by_building.setdefault(alarm["building"], []).append(alarm)

# print(group_by_building)

#group by severity:

# alarms = [
#     {"severity": "HIGH"},
#     {"severity": "LOW"},
#     {"severity": "HIGH"},
#     {"severity": "CRITICAL"},
#     {"severity": "HIGH"}
# ]

# group_by_severity = {}

# for alarm in alarms:
#     group_by_severity.setdefault(alarm["severity"], []).append(alarm)

# print(group_by_severity)

#batch 4: functions and return

#input
# input = [
#     {"severity": "HIGH"},
#     {"severity": "LOW"},
#     {"severity": "HIGH"}
# ]

# severity = []

# def get_high_alarms(alarms):
#     for alarm in alarms:
#         if alarm["severity"] == "HIGH":
#             severity.append(alarm)
#     return severity

# print(get_high_alarms(input))

# alarms = [{"building": "Chruch", "owner": "Jesus"},
#         {"building": "API Technologies", "owner": "Arsh"},
#         {"building": "API Technologies", "owner": "Arsh"}]

# count = 0
# unique_buildings = set()

# def count_buildings(alarms):
#     for alarm in alarms:
#         if alarm["building"] in unique_buildings:
#             continue
#         unique_buildings.add(alarm["building"])
#     return len(unique_buildings)

# print(count_buildings(alarms))

#batch 5 sliding window
# temps = [20, 30, 31, 32, 15]

# def check_temps(temps):
#     for i in range(len(temps) - 2):
#         if temps[i] > 25 and temps[i+1] > 25 and temps[i+2] > 25:
#             return True
#     return False
    
# print(check_temps(temps))

# results = [
#     "PASS",
#     "FAIL",
#     "PASS",
#     "FAIL",
#     "FAIL"
# ]

# def three_fails(results):
#     for i in range(len(results)-2):
#         if results[i] == "FAIL" and results[i+1] == "FAIL" and results[i+2] == "FAIL":
#             return True
#     return False

# print(three_fails(results))

# I am skipping one

#batch 6 --> mini alarm detector
# alarms = [
#     {"severity": "LOW"},
#     {"severity": "CRITICAL"},
#     {"severity": "HIGH"}
# ]

# def detect_critical(alarms):
#     for alarm in alarms:
#         if alarm["severity"] == "CRITICAL":
#             return True
        
# print(detect_critical(alarms))


#alarm summary
# alarms = [
#     {"severity": "HIGH"},
#     {"severity": "HIGH"},
#     {"severity": "LOW"}
# ]

# summary= {}

# def alarm_summary(alarms):
#     count = 0
#     low = 0
#     summary["total"] = len(alarms)
#     for alarm in alarms:
#         if alarm["severity"] == "HIGH":
#             count+=1
#         else:
#             low+=1
        
#     summary["high"] = count
#     summary["low"] = low

#     return summary

# print(alarm_summary(alarms))

#device health check

input = [
    {"device": "RTU", "status": "ONLINE"},
    {"device": "AHU", "status": "OFFLINE"},
    {"device": "VAV", "status": "ONLINE"}
]

def device_check(devices):
    for device in devices:
        if device["status"] == "OFFLINE":
            return device["device"]
        
print(device_check(input))