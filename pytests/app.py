def count_high_alarms(alarms):

    count = 0

    for alarm in alarms:
        if alarm["severity"] == "HIGH":
            count+=1

    return count


def count_critical_alarms(alarms):
    count = 0

    for alarm in alarms:
        if alarm["severity"] == "CRITICAL":
            count+=1
    return count

def find_offline_devices(devices):
    offline_devices = []

    for device in devices:
        if device["status"] == "OFFLINE":
            offline_devices.append(device["device"])

    return offline_devices

def has_duplicates(devices):
    dups = set()

    for device in devices:
        if device in dups:
            return True
        dups.add(device)
    return False