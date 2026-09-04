from collections import defaultdict

alarms = {}

alarms.setdefault("HIGH", []).append("AHU-01")
alarms.setdefault("HIGH",[]).append("AHU-02")

print(dict(alarms))