import requests
import pytest
from unittest.mock import patch

def get_alarm_count():

    response = requests.get(
        "https://api.company.com/alarms"
    )

    if response.status_code != 200:
        return None

    return response.json()["count"]


@pytest.mark.parametrize(
    "status_code, data, expected",
    [
        (200, {"count": 0}, 0),
        (200, {"count": 5}, 5),
        (500, {}, None)
    ]
)
@patch("requests.get")
def test_get_alarm_count(mock_get, status_code, data, expected):

    mock_get.return_value.status_code = status_code
    mock_get.return_value.json.return_value = data
    result = get_alarm_count()

    assert result == expected