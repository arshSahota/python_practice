import pytest

controllers = [
    {"controller": "CTRL-01", "connected": True, "devices": 12},
    {"controller": "CTRL-02", "connected": False, "devices": 8},
    {"controller": "CTRL-03", "connected": True, "devices": 0},
    {"controller": "CTRL-04", "connected": False, "devices": 0},
]

def analyze_controllers(controllers):
    healthy = []
    unhealthy = []
    invalid = []
    most_devices = {}
    healthy_count = 0

    for controller in controllers:
        reasons = []

        if "connected" not in controller:
            invalid.append({
                "controller": controller.get("controller"),
                "reason": "MISSING_CONNECTED"
            })
            continue

        if "devices" not in controller:
            invalid.append({
                "controller": controller.get("controller"),
                "reason": "MISSING_DEVICES"
            })
            continue

        if controller["connected"] is True and controller["devices"] > 0:
            if controller["devices"] > healthy_count:
                most_devices["controller"] = controller["controller"]
                most_devices["devices"] = controller["devices"]

                healthy_count = controller["devices"]

            healthy.append({
                "controller": controller.get("controller")
            })

        if controller["connected"] is False:
            reasons.append("DISCONNECTED")

        if controller["devices"] <= 0:
            reasons.append("NO_DEVICES")

        if reasons:
            unhealthy.append({
                "controller": controller.get("controller"),
                "reason": reasons
            })

    return {
        "healthy": healthy,
        "unhealthy": unhealthy,
        "healthy_count": len(healthy),
        "unhealthy_count": len(unhealthy),
        "invalid": invalid,
        "most_devices": most_devices
    }

print(analyze_controllers(controllers))

def test_healthy_controller():
    data = [{"controller": "A", "connected": True, "devices": 5}]

    result = analyze_controllers(data)

    assert result["healthy"] == [{"controller": "A"}]


def test_disconnected_controller():
    data = [{"controller": "A", "connected": False, "devices": 5}]
    
    result = analyze_controllers(data)
    
    assert result["unhealthy"] == [{"controller": "A", "reason": ["DISCONNECTED"]}]

def test_no_devices():

    data = [{"controller": "A", "connected": True, "devices": 0}]
    
    result = analyze_controllers(data)
    
    assert result["unhealthy"] == [{"controller": "A", "reason": ["NO_DEVICES"]}]

def test_no_devices_disconnected():
    data = [{"controller": "A", "connected": False, "devices": 0}]
    
    result = analyze_controllers(data)
    
    assert result["unhealthy"] == [{"controller": "A", "reason": ["DISCONNECTED", "NO_DEVICES"]}]
    

def test_missing_connected_filed():
    data = [{"controller": "A", "devices": 5}]
    
    result = analyze_controllers(data)
    
    assert result["invalid"] == [{"controller": "A", "reason": "MISSING_CONNECTED"}]

def test_controller_with_most_devices():
    data = [{"controller": "A", "connected": True, "devices": 5},
            {"controller": "B", "connected": True, "devices": 10},
            {"controller": "C", "connected": True, "devices": 48}]
    
    result = analyze_controllers(data)
    
    assert result["most_devices"] == {"controller": "C", "devices": 48}