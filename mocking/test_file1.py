# from unittest.mock import patch

# def get_device_status():
#     return "online"

# def is_device_healthy():
#     status = get_device_status()

#     return status == "online"

# @patch("test_file1.get_device_status")
# def test_device_healthy(mock_status):

#     mock_status.return_value = "online"

#     assert is_device_healthy() is True