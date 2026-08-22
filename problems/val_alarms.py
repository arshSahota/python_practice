events = [
    {"device": "AHU-01", "severity": "HIGH"},
    {"device": "VAV-01", "severity": "LOW"},
    {"device": "AHU-02", "severity": "CRITICAL"},
    {"device": "VAV-02", "severity": "MEDIUM"},
    {"device": "AHU-03", "severity": "CRITICAL"}
]

def analyze_events(events):

    escalated  = []
    normal = []
    invalid = []
    high_count = 0
    critical_count = 0

    for event in events:

        if "severity" not in event:
            invalid.append({
                "device": event["device"],
                "reason": "MISSING Severity"
            })
            continue

        if event["severity"] not in ["MEDIUM", "HIGH", "LOW", "CRITICAL"]:
            invalid.append({
                "device": event["device"],
                "reason": "INVALID_SEVERITY"
            })
            continue

        device = event["device"]
        severity = event["severity"]

        if severity in ["HIGH", "CRITICAL"]:
            escalated.append({
                "device": device
            })

            if severity == "HIGH":
                high_count+=1

            if severity == "CRITICAL":
                critical_count+=1

        else:
            normal.append({
                "device": device
            })

    return {
        "escalated": escalated,
        "normal": normal,
        "high_count": high_count,
        "critical_count": critical_count,
        "invalid": invalid
    }


print(analyze_events(events))

def test_escalated_devices():

    result = analyze_events(events)

    assert len(result["escalated"]) == [
        {"device": "AHU-01"},
        {"device": "AHU-02"},
        {"device": "AHU-03"}
    ]

def test_severity_counts():

    result = analyze_events(events)

    assert result["high_count"] == 1
    assert result["critical_count"] == 2

def test_missing_severity():

    test_events = [
        {"device": "AHU-05"}
    ]

    result = analyze_events(test_events)

    assert result["invalid"] == [
        {
            "device": "AHU-05",
            "reason": "MISSING_SEVERITY"
        }
    ]

def test_invalid_severity():

    test_events = [
        {
            "device": "AHU-06",
            "severity": "URGENT"
        }
    ]

    result = analyze_events(test_events)

    assert result["invalid"] == [
        {
            "device": "AHU-06",
            "reason": "INVALID_SEVERITY"
        }
    ]

