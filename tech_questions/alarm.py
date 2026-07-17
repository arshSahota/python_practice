def alarm_requires_acknowledgement(
    severity,
    acknowledged
):
    if severity == "CRITICAL":
        return acknowledged

    return True