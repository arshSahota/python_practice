import pytest
import requests
from unittest.mock import patch

# @pytest.fixture
# def device():

#     return {
#         "device": "AHU-01",
#         "status": "online",
#         "alarms": 0
#     }

# def test_device_status(device):
#     assert device["status"] == "online"

# def test_alarms_count(device):
#     assert device["alarms"] == 0

# we use fixtures because they provide us with reusable test data or set up so you do not repeat the same code in every test.

# fixture = "prepare something for my test"

#parametrize
#run one test with multiple inputs

# def is_valid(temp):

#     return 0 <= temp <= 50

# @pytest.mark.parametrize(
#     "temp, expected",
#     [
#         (-5, False),
#         (20, True),
#         (50, True),
#         (60, False)
#     ]
# )
# def test_temperature_validation(temp, expected):

#     assert is_valid(temp) == expected

## we use parametrization in pytest to run the same test with different inputs without repeating code

#Paramerization ==> Run this same test with multiple sets of data

##mocking

## when we want to fake an API, DB, hardware device, service etc

# def get_alarm_count():
#     return 3

# def has_alarms():

#     return get_alarm_count() > 0

# @patch("test_file2.get_alarm_count")
# def test_has_alarms(mock_count):

#     mock_count.return_value = 10

#     assert has_alarms() is True

##mocking replaces a real dependency with a fake one

## API TESTING

def get_user():

    response = requests.get("https://api.example.cpm/user/1")

    return response.json()

@patch("requests.get")
def test_get_user(mock_get):

    mock_get.return_value.json.return_value = {
        "id": 1,
        "name": "Arshdeep"
    }

    result = get_user()

    assert result["id"] == 1