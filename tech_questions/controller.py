def determine_controller_status(cpu, memory):
    if cpu > 90 or memory > 90:
        return "CRITICAL"

    elif cpu >= 80 or memory >= 80:
        return "WARNING"

    return "HEALTHY"