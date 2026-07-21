# import pytest

# response = {
#     "status_code": 200,
#     "data": {
#         "controller_id": "CTRL-001",
#         "cpu": 95,
#         "memory": 45,
#         "status": "CRITICAL"
#     }
# }

#validate schema
# def test_response():
#     assert response["status_code"] == 200
#     data = response["data"]

#     assert "controller_id" in data
#     assert "cpu" in data
#     assert "memory" in data
#     assert "status" in data

#validate the business rule
# def test_response():
#     assert response["status_code"] == 200

#     data = response["data"]

#     assert "controller_id" in data

#     if data["cpu"] >= 90 or data["memory"] >= 90:
#         assert data["status"]== "CRITICAL"
