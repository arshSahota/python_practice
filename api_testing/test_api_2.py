# response_status_code = 200

# response_body = [
#     {
#         "id": 101,
#         "building": "Surrey HQ",
#         "type": "Temperature",
#         "severity": "High",
#         "status": "Open",
#         "timestamp": "2026-07-09T12:30:00Z"
#     },
#     {
#         "id": 102,
#         "building": "Burnaby Office",
#         "type": "Humidity",
#         "severity": "Medium",
#         "status": "Closed",
#         "timestamp": "2026-07-09T13:15:00Z"
#     }
# ]

# def test_severity():
#     valid_severities = {"Low", "Medium", "High", "Critical"}

#     for alarm in response_body:
#         assert alarm["severity"] in valid_severities, f"Invalid Severity found: {alarm['severity']}"


# def test_valid_status():

#     valid_statuses = {"Open", "Closed", "Acknowledged"}

#     for alarm in response_body:
#         assert alarm["status"] in valid_statuses, f"{alarm['id']} has invalid status code of {alarm['status']}"

# def test_required_fields():
#     required_fields = {"id", "building", "type", "severity", "status", "timestamp"}

#     for alarm in response_body:
#         missing_fields = required_fields - set(alarm.keys())

#         assert not missing_fields, (f"Alarm ID {alarm.get('id', 'Unknown')} is missing fields: {missing_fields}")