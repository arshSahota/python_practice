import pytest

dashboard_data = [
    {"site": "BuildingA", "online_devices": 12, "offline_devices": 0},
    {"site": "BuildingB", "online_devices": 8, "offline_devices": 3},
    {"site": "BuildingC", "online_devices": 15, "offline_devices": 0},
    {"site": "BuildingD", "online_devices": 9, "offline_devices": 1}
]

def validate_dashboard(dashboard_data):
    result = {}

    result["healthy"] = []
    result["unhealthy"] = []
    result["missing_data"] = []

    total_offline = 0

    for dash in dashboard_data:

        if not "site" in dash:
            result["missing_data"].append({
                "site": "UNKNOWN",
                "online_devices": dash["online_devices"],
                "offline_devices": dash["offline_devices"]
            })
            continue

        if not "online_devices" in dash:
            result["missing_data"].append({
                "site": dash["site"],
                "reason": "MISSING_ONLINE_DEVICES",
            }) 
            continue

        if not "offline_devices" in dash:
            result["missing_data"].append({
                "site": dash["site"],
                "reason": "MISSING_OFFLINE_DEVICES"
            })
            continue

        site = dash["site"]
        online = dash["online_devices"]
        offline = dash["offline_devices"]

        if offline == 0:

            result["healthy"].append({
                "site": site
            })

        else:
            result["unhealthy"].append({
                "site": site,
                "offline_devices": offline
            })
            total_offline+=offline

    return {
        "healthy": result["healthy"],
        "unhealthy": result["unhealthy"],
        "healthy_count": len(result["healthy"]),
        "unhealthy_count": len(result["unhealthy"]),
        "total_offline": total_offline,
        "missing_data": result["missing_data"]
    }

print(validate_dashboard(dashboard_data))

def test_healthy_site():
    data = [{
        "site": "BuildingA",
        "online_devices": 12,
        "offline_devices": 0
    }]

    result = validate_dashboard(data)

    assert result["healthy"] == [{"site": "BuildingA"}]

def test_unhealthy_site():
    data = [{
        "site": "BuildingB",
        "online_devices": 0,
        "offline_devices": 12
    }]

    result = validate_dashboard(data)

    assert result["unhealthy"] == [{"site": "BuildingB", "offline_devices": 12}]

def test_missing_offline_devices():
    data = [{
        "site": "BuildingC",
        "online_devices": 11
    }]

    result = validate_dashboard(data)

    assert result["missing_data"] == [{"site": "BuildingC", "reason": "MISSING_OFFLINE_DEVICES"}]