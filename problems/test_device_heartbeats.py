import pytest

heartbeats = [
    {"device": "AHU-01", "last_seen": 2},
    {"device": "VAV-01", "last_seen": 15},
    {"device": "AHU-02", "last_seen": 4},
    {"device": "VAV-02", "last_seen": 20},
]

def analyze_heartbeats(heartbeats):
    online = []
    offline = []
    missing_data = []
    long_time = 0
    longest_offline = {}

    for device in heartbeats:

        if not "last_seen" in device:
            missing_data.append({
                "device": device["device"],
                "reason": "MISSING_LAST_SEEN"
            })
            continue

        dev = device["device"]
        last_seen = device["last_seen"]

        if last_seen > 5 and last_seen > long_time:
            long_time = last_seen
            longest_offline = {
                "device": dev,
                "last_seen": last_seen
            }

        if last_seen <= 5:
            online.append({
                "device": dev,
            })
        else:
            offline.append({
                "device": dev,
                "last_seen": last_seen
            })

    return {
        "online": online,
        "offline": offline,
        "online_count": len(online),
        "offline_count": len(offline),
        "missing_data": missing_data,
        "longest_offline": longest_offline
    }

print(analyze_heartbeats(heartbeats))

def test_online_device():
    data = [{"device": "AVH-07", "last_seen": 2}]
    result = analyze_heartbeats(data)

    assert result["online"] == [{"device": "AVH-07"}]

def test_offline_device():
    data = [{"device": "AVH-15", "last_seen": 9}]
    result = analyze_heartbeats(data)

    assert result["offline"] == [{"device": "AVH-15", "last_seen": 9}]

def test_missing_data():
    data = [{"device": "AVH-17"}]
    result = analyze_heartbeats(data)

    assert result["missing_data"] == [{"device": "AVH-17", "reason": "MISSING_LAST_SEEN"}]