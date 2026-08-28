from unittest.mock import patch

def get_alarm_count():
    return 3


def system_has_active_alarms():
    return get_alarm_count() > 0

@patch("test_file3.get_alarm_count")
def test_alarm_count(mock_count):
    mock_count.return_value = 10
    assert system_has_active_alarms() is True

@patch("test_file3.get_alarm_count")
def test_alarm_count2(mock_count):
    mock_count.return_value = 0
    assert system_has_active_alarms() is False