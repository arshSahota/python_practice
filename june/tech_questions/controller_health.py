
controllers = [
    {
        "id": "CTRL-001",
        "cpu": 45,
        "memory": 50
    },
    {
        "id": "CTRL-002",
        "cpu": 95,
        "memory": 40
    },
    {
        "id": "CTRL-003",
        "cpu": 70,
        "memory": 92
    },
    {
        "id": "CTRL-004",
        "cpu": 60,
        "memory": 55
    }
]

def determine_controller_status(cpu, mem):
    if cpu >= 90 or mem >= 90:
        return "CRITICAL"
    return "HEALTHY"

def summarize_controllers(controllers):

    healthy = []
    critical = []

    for controller in controllers:
        id = controller["id"]
        cpu = controller["cpu"]
        mem = controller["memory"]


        if cpu >= 90 or mem >= 90:
            critical.append(id)

        else:
            healthy.append(id)

    return {
        "healthy": healthy,
        "critical": critical
    }

