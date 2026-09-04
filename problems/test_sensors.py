import pytest

sensors = [
    {"sensor": "Room1", "status": "online", "temperature": 22},
    {"sensor": "Room2", "status": "offline", "temperature": 25},
    {"sensor": "Room3", "status": "online", "temperature": 60},
    {"sensor": "Room4", "status": "offline", "temperature": 70},
    {"sensor": "Room5", "status": "online"}
]

def analyze_sensors(sensors):

    healthy = []
    unhealthy = []
    hottest_valid = {}
    hottest_temp = 0

    for sensor in sensors:

        reasons = []

        sensor_name = sensor["sensor"]
        status = sensor.get("status")
        temp = sensor.get("temperature")

        if status is None:
            reasons.append("MISSING_STATUS")

        if temp is None:
            reasons.append("MISSING_TEMPEARTURE")

        if status == "offline":
            reasons.append("OFFLINE")

        if temp is not None and (temp < 0 or temp > 50):
            reasons.append("INVALID_TEMPERATURE")

        if not reasons:
            if temp > hottest_temp:
                hottest_temp = temp

                hottest_valid["sensor"] = sensor_name
                hottest_valid["temperature"] = temp

            healthy.append({
                "sensor": sensor_name
            })
        else:
            unhealthy.append({
                "sensor": sensor_name,
                "reason": reasons
            })

    
    return {
        "healthy": healthy,
        "unhealthy": unhealthy,
        "healthy_count": len(healthy),
        "unhealthy_count": len(unhealthy),
        "hottest_valid": hottest_valid
    }

print(analyze_sensors(sensors))

def test_healthy_sensor():

    data = [{"sensor": "Room6", "status": "online", "temperature": 22}]

    result = analyze_sensors(data)

    assert result["healthy"] == [{"sensor": "Room6"}]

def test_offline_sensor():

    data = [{"sensor": "Room7", "status": "offline", "temperature": 30}]

    result = analyze_sensors(data)

    assert result["unhealthy"] == [{"sensor": "Room7", "reason": ["OFFLINE"]}]

def test_invalid_temperature():

    data = [{"sensor": "Room8", "status": "online", "temperature": 70}]

    result = analyze_sensors(data)

    assert result["unhealthy"] == [{"sensor": "Room8", "reason": ["INVALID_TEMPERATURE"]}]

def test_offline_invalid_temperature():

    data = [{"sensor": "Room9", "status": "offline", "temperature": 80}]

    result = analyze_sensors(data)

    assert result["unhealthy"] == [{"sensor": "Room9", "reason": ["OFFLINE", "INVALID_TEMPERATURE"]}]

def test_missing_temp():

    data = [{"sensor": "Room10", "status": "online"}]

    result = analyze_sensors(data)

    assert result["unhealthy"] == [{"sensor": "Room10", "reason": ["MISSING_TEMPEARTURE"]}]