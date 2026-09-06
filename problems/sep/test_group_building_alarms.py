from collections import defaultdict
import pytest

events = [
    {"device": "AHU-01", "severity": "HIGH"},
    {"device": "VAV-01", "severity": "LOW"},
    {"device": "AHU-02", "severity": "HIGH"},
    {"device": "VAV-02", "severity": "MEDIUM"},
    {"device": "AHU-03", "severity": "CRITICAL"},
    {"device": "VAV-03", "severity": "LOW"},
]

def group_alarms(events):
    grouped = defaultdict(list)
    counts = defaultdict(int)
    invalid = []
    ##missing severity add under "invalid", add device, reason
    ##missing device, add under "invalid", add severity, and reason
    for event in events:

        if "severity" not in event:
            invalid.append({
                "device": event.get("device", "UNKNOWN"),
                "reason": "MISSING_SEVERITY"
            })
            continue

        if "device" not in event:
            invalid.append({
                "device": "UNKNOWN",
                "reason": "MISSING_DEVICE"
            })
            continue

        grouped[event["severity"]].append(event["device"])
        counts[event["severity"]]+=1

    return {
        "grouped": dict(grouped),
        "counts": dict(counts),
        "invalid": invalid
    }

print(group_alarms(events))

def test_high_count():

    result = group_alarms(events)

    assert result["counts"]["HIGH"] == 2

def test_low_count():

    result = group_alarms(events)

    assert result["counts"]["LOW"] == 2

def test_missing_severity():

    data = [{"device": "LALALA"}]

    result = group_alarms(data)

    assert result["invalid"] == [{"device": "LALALA", "reason": "MISSING_SEVERITY"}]

def test_missing_device():

    data = [{"severity": "HIGH"}]

    result = group_alarms(data)

    assert result["invalid"] == [{"device": "UNKNOWN", "reason": "MISSING_DEVICE"}]