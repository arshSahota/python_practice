from alarms import get_alarm_status

def test_critical_alarm():
    assert get_alarm_status("Critical") == "Open"

def test_medium_alarm():
    assert get_alarm_status("Medium") == "Closed"