devices = [
    {
        "device_id": "SW-001",
        "cpu": 45,
        "memory": 50,
        "online": True,
        "ip_addresses": [
            "10.0.0.1",
            "10.0.0.2"
        ]
    },
    {
        "device_id": "SW-002",
        "cpu": 95,
        "memory": 60,
        "online": True,
        "ip_addresses": [
            "10.0.0.3"
        ]
    },
    {
        "device_id": "SW-003",
        "cpu": 65,
        "memory": 92,
        "online": False,
        "ip_addresses": [
            "10.0.0.4"
        ]
    },
    {
        "device_id": "SW-004",
        "cpu": 35,
        "memory": 40,
        "online": True,
        "ip_addresses": [
            "10.0.0.2"
        ]
    }
]

def analyse_devices(devices):

    healthy_devices = set()
    critical_devices = set()
    defective_devices = {}
    all_ips = set()

    for device in devices:
        device_id = device["device_id"]
        cpu = device["cpu"]
        memory = device["memory"]

        if cpu < 90 and memory < 90 and device["online"] is True:
            healthy_devices.add(device_id)

        if cpu >= 90 or memory >= 90:
            critical_devices.add(device_id)

        if device["online"] is False:
            defective_devices.setdefault(device_id, []).append("Device Offline")
        
        for ip in device["ip_addresses"]:
            if ip in all_ips:
                defective_devices.setdefault(device_id, []).append("Duplicate IP")
            all_ips.add(ip)

    return {
        "healthy_devices": healthy_devices,
        "critical_devices": critical_devices,
        "defective_devices": defective_devices,
        "all_ips": all_ips
    }

print(analyse_devices(devices))