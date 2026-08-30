# from unittest.mock import patch
# import requests

# def get_device():

#     response = requests.get("api/devices/1")

#     return response.json()


# @patch("requests.get")
# def test_get_device(mock_get):

#     mock_get.return_value.json.return_value = {
#         "device": "AHU-01",
#         "status": "online"
#     }

#     result = get_device()

#     assert result["status"] == "online"