from temp import classify_temp
import pytest

@pytest.fixture
def high_temp_sensor():
    return {
        "room": "Mechanical Room",
        "temperature": 35,
        "alarm": True
    }

def test_sensor_has_high_temperature(high_temp_sensor):
    assert high_temp_sensor["temperature"] > 30


def test_sensor_alarm_is_on(high_temp_sensor):
    assert high_temp_sensor["alarm"] == True

#question:
#ans one place
