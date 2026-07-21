import pytest 

events = [
    {
        "building": "North Tower",
        "alarm_type": "HIGH_TEMP",
        "severity": "CRITICAL",
        "acknowledged": False
    },
    {
        "building": "North Tower",
        "alarm_type": "HIGH_TEMP",
        "severity": "CRITICAL",
        "acknowledged": True
    },
    {
        "building": "South Tower",
        "alarm_type": "LOW_TEMP",
        "severity": "WARNING",
        "acknowledged": True
    },
    {
        "building": "East Tower",
        "alarm_type": "POWER_FAILURE",
        "severity": "CRITICAL",
        "acknowledged": False
    },
    {
        "building": "East Tower",
        "alarm_type": "POWER_FAILURE",
        "severity": "CRITICAL",
        "acknowledged": False
    }
]

def analyse_alarms(events):

    critical_unacknowledged = {}
    duplicate_alarms = {}
    buildings = set()
    alarm_counts = {}
    alarm_occurences = {}

    for event in events:
        building = event["building"]
        alarm = event["alarm_type"]
        severity = event["severity"]
        ack_status = event["acknowledged"]

        alarm_key = (building, alarm, severity)

        alarm_occurences[alarm_key] = alarm_occurences.get(alarm_key, 0) + 1

        if severity == "CRITICAL" and ack_status is False:
            critical_unacknowledged.setdefault(building, []).append(alarm)
    
    for alarm_key, count in alarm_occurences.items():
        if count > 1:
            building, alarm, severity = alarm_key

            duplicate_alarms[(building, alarm)] = count

    return {
        "critical_unacknowledged": critical_unacknowledged,
        "duplicate_alarms": duplicate_alarms,
        "buildings": buildings,
        "alarm_counts": alarm_counts
    }

print(analyse_alarms(events))