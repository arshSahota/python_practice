controllers = [
    {
        "id": "CTRL-001",
        "firmware": "5.2.0",
        "online": True
    },
    {
        "id": "CTRL-002",
        "firmware": "4.9.1",
        "online": True
    },
    {
        "id": "CTRL-003",
        "firmware": "5.1.0",
        "online": False
    },
    {
        "id": "CTRL-004",
        "firmware": "5.3.1",
        "online": True
    }
]

def validate_controllers(controllers):
    compliant = []
    non_compliant = {}

    for controller in controllers:
        id = controller["id"]
        firmware = controller["firmware"]
        status = controller["online"]

        if firmware.startswith("5") and status is True:
            compliant.append(id)
        elif not (firmware.startswith("5")):
            non_compliant[id] = "Unsupported Firmware"
        else:
            non_compliant[id] = "Controller Offline"

    return{
        "compliant": compliant,
        "non_compliant": non_compliant
    }

print(validate_controllers(controllers))