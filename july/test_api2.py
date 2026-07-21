# import pytest

# response = {
#     "status_code": 200,
#     "data": {
#         "controller_id": "CTRL-001",
#         "cpu": 95,
#         "memory": 45,
#         "status": "HEALTHY"
#     }
# }

# #layer one

# def test_response():
#     assert response["status_code"] == 200

#     data = response["data"]

#     assert "controller_id" in data
#     assert "cpu" in data
#     assert "memory" in data
#     assert "status" in data

#     assert isinstance(data["controller_id"], str)
#     assert isinstance(data["cpu"], int)
#     assert isinstance(data["memory"], int)
#     assert isinstance(data["status"], str)

#     if data["cpu"] >= 90 or data["memory"] >= 90:
#         assert data["status"] == "CRITICAL"

    #yes API responded successfully
    #yes all expected fields exist
    #yes APU returned correcr data types




