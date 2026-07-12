import pytest

@pytest.fixture
def valid_sensor_response():
    return {
        "building": "North Tower",
        "temperature": 35,
        "alarm": True,
        "energy_usage": 1200
    }

@pytest.fixture
def invalid_sensor_response():
    return {
        "building": "",
        "temperature": 35,
        "alarm": True,
        "energy_usage": -500
    }

@pytest.fixture
def low_temp_sensor():
    return {
        "building": "South Tower",
        "temperature": 15,
        "alarm": False,
        "energy_usage": 700
    }