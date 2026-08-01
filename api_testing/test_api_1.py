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
#         "severity": "Low",
#         "status": "Closed",
#         "timestamp": "2026-07-09T13:15:00Z"
#     }
# ]

# def test_status_code():
#     assert response_status_code == 200

# def test_response_is_list():
#     assert isinstance(response_body, list)

# def test_required_fields_exist():
#     required_fields = {"id", "building", "type", "severity", "status","timestamp"}

#     for alarm in response_body:
#         assert required_fields.issubset(alarm.keys())

# def test_valid_severity_values():

#     valid_severities = {"Low", "Medium", "High", "Critical"}
#     for alarm in response_body:
#         assert alarm["severity"] in valid_severities

# def test_valid_status_values():
#     valid_statuses = {"Open", "Closed", "Acknowledged"}

#     for alarm in response_body:
#         assert alarm["status"] in valid_statuses
    

